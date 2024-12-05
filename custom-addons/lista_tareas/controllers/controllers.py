# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json


class ListaTareas(http.Controller):
    @http.route('/lista_tareas/lista_tareas', auth='public')
    def index(self, **kw):
        return "Hola soy Fabio"

    @http.route('/lista_tareas/lista_tareas/objects', auth='public')
    def list(self, **kw):
        return http.request.render('lista_tareas.listing', {
            'root': '/lista_tareas/lista_tareas',
            'objects': http.request.env['lista_tareas.lista_tareas'].search([]),
        })

    @http.route('/lista_tareas/lista_tareas/objects/<model("lista_tareas.lista_tareas"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('lista_tareas.object', {
            'object': obj
        })

    @http.route('/lista_tareas/lista_tareas/listado', auth='public', csrf=False, type='http', methods=['GET'])
    def liston(self, **kw):
        tareas = request.env['lista_tareas.lista_tareas'].search([])

        lista_tareas = []
        for tarea in tareas:
            lista_tareas.append({
                'id': tarea.id,
                'tarea': tarea.tarea,
                'prioridad': tarea.prioridad,
                'urgente': tarea.urgente,
                'realizada': tarea.realizada,
            })
        return request.make_response(json.dumps(lista_tareas), headers={'Content-Type': 'application/json'})