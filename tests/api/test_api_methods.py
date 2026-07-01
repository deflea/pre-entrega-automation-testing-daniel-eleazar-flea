import logging
import os
import pytest_check as check
from api.api_functions import get_users, get_all_posts, create_post, update_post, delete_post


logger = logging.getLogger(__name__)

def test_get_users():
    logger.info('Iniciando test_get_users')
    response = get_users()
    
    check.equal(response.status_code, 200)
    data = response.json()
    
    check.greater(len(data), 0)
    logger.info('test_get_users completado con éxito')

def test_get_all_posts():
    logger.info('Iniciando test_get_all_posts')
    response = get_all_posts()
    
    check.equal(response.status_code, 200)
    data = response.json()
    
    check.greater(len(data), 0)
    logger.info('test_get_all_posts completado con éxito')

def test_create_post():
    logger.info('Iniciando test_create_post')
    
    title_test = "Prueba de automatizacion"
    body_test = "Contenido del post para el proyecto final"
    user_id_test = 1
    
    response = create_post(title_test, body_test, user_id_test)
    
    check.equal(response.status_code, 201)
    res_data = response.json()
    
    check.equal(res_data.get("title"), title_test)
    check.equal(res_data.get("body"), body_test)
    check.equal(res_data.get("userId"), user_id_test)
    logger.info('test_create_post completado con éxito')

def test_update_post():
    logger.info('Iniciando test_update_post')
    
    post_id = 1
    nuevo_title = "Titulo Actualizado"
    nuevo_body = "Cuerpo del post modificado"
    user_id = 1
    
    updated_response = update_post(post_id, nuevo_title, nuevo_body, user_id)
    
    check.equal(updated_response.status_code, 200)
    res_data = updated_response.json()
    
    check.equal(res_data.get("title"), nuevo_title)
    check.equal(res_data.get("body"), nuevo_body)
    logger.info('test_update_post completado con éxito')

def test_delete_post():
    logger.info('Iniciando test_delete_post')
    post_id = 1
    
    delete_response = delete_post(post_id)

    check.equal(delete_response.status_code, 200)
    logger.info('test_delete_post completado con éxito')