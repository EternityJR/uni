from xml.etree.ElementTree import fromstring
from xmljson import badgerfish as bf
import re
from model import Terms, Types, Links, connect_db, close_db, create_types, db
import configparser
import json
import cherrypy


def parse_xml():
    a = open('DFD.xml', encoding='UTF-8').read()
    bf.dict = dict
    res = bf.data(fromstring(a))

    list_of_elems = res['mxGraphModel']['root']['mxCell']
    for elem in list_of_elems[2:]:
        if not elem.get('@target') and not elem.get('@source'):
            Terms.create(xml_id=elem['@id'], value=elem['@value'], style=elem['@style'])
    for elem in list_of_elems[2:]:
        if elem.get('@target') or elem.get('@source'):
            source = Terms.get(xml_id=elem['@source'])
            target = Terms.get(xml_id=elem['@target'])
            value = elem['@value']
            type_id = Types.get(1)
            if ("ellipse" in source.style) and ("ellipse" in target.style):
                type_id = Types.get(id=2)
            if (("ellipse" in source.style) and ("shape" in target.style)) or (
                    ("shape" in source.style) and ("ellipse" in target.style)):
                type_id = Types.get(id=3)
            if ("ellipse" in source.style) and ("ellipse" in target.style):
                type_id = Types.get(id=2)
            Links.create(source_id=source, target_id=target, link_type_id=type_id, value_arrow=value)


class Web:
    """Contains a number of functions which allow manage entries in database"""
    @cherrypy.expose
    def index(self):
        raise cherrypy.HTTPRedirect("/static/")

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def get_all_data(self):
        j_notes = []
        test = len(Terms.select(Terms.id, Terms.value, Terms.description).where(Terms.id > 0))
        for i in range(test):
            temp = Terms.get(i+1)
            j_notes.append((temp.id, temp.value, '' if temp.description is None else temp.description))
        return json.dumps(j_notes)


    @cherrypy.expose
    @cherrypy.tools.json_in()
    def get_one_entry(self, id):
        temp = Terms.get_by_id(id)
        return json.dumps((temp.id, temp.value, temp.description))


    @cherrypy.expose
    def update_entry(self, id, value, description):
        temp = Terms.get_or_none(Terms.id == id)
        Terms.update(description=description).where(Terms.id == temp.id).execute()
        raise cherrypy.HTTPRedirect('/static/')


    @cherrypy.expose
    @cherrypy.tools.json_in()
    def get_all_links(self):
        j_notes = []
        temp = Links.select().where(Links.id > 0)
        for i in temp:
            main_term = Terms.get(id=i.source_id).value
            target_term = Terms.get(id=i.target_id).value
            type_name = Types.get(id=i.link_type_id).type_name
            j_notes.append((i.id, main_term, target_term, type_name))
        return json.dumps(j_notes)


    @cherrypy.expose
    @cherrypy.tools.json_in()
    def get_all_types(self):
        j_notes = []
        test = len(Types.select(Types.id, Types.type_name, Types.source_name, Types.target_name).where(Types.id > 0))
        for i in range(test):
            temp = Types.get(i+1)
            j_notes.append((temp.id, temp.type_name, temp.source_name, temp.target_name))
        return json.dumps(j_notes)


    @cherrypy.expose
    @cherrypy.tools.json_in()
    def get_links_for_term(self, id):
        j_notes = []
        temp = Links.select().where((Links.source == id) | (Links.target == id))
        for i in temp:
            print(i.source, " ", i.target)
            if (Links.get(source=id).source == i.source):
                term_1 = Terms.get_by_id(i.source).value
                link = Types.get(id=i.link_type_id).source_name
                term_2 = Terms.get_by_id(i.target).value
                print(term_1, " ", link, " ", term_2)
                j_notes.append((term_1, link, term_2))


            elif (Links.get(target=id).target == i.target):
                term_1 = Terms.get_by_id(i.target).value
                link = Types.get(id=i.link_type_id).target_name
                term_2 = Terms.get_by_id(i.source).value
                print(term_1, " ", link, " ", term_2)
                j_notes.append((term_1, link, term_2))
        return json.dumps(j_notes)


def main():
    connect_db()
    create_types()
    parse_xml()

    config = configparser.ConfigParser()
    config.read('settings.ini', encoding='UTF-8')

    cherrypy.quickstart(Web(), "/",
                        {'global': {'server.socket_host': config["Server"]["host"],
                                    'server.socket_port': int(config["Server"]["port"]),
                                    'tools.staticdir.root': config["Path"]["static_dir_root"],
                                    'log.error_file': 'site.log'},
                        '/static': {
                             'tools.staticdir.on': True,
                             'tools.staticdir.dir': 'static',
                             'tools.staticdir.index': 'index.html',
                        }})
    close_db()


if __name__ == "__main__":
    main()