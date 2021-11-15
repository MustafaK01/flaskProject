from crypt import methods
from re import A
from MySQLdb.cursors import Cursor
from flask import Flask,render_template,flash,redirect,url_for,request,session
from wtforms import Form,StringField,PasswordField,validators
from passlib.handlers.sha2_crypt import sha256_crypt
from flask_mysqldb import MySQL
import sqlite3
from wtforms.fields import choices
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import EmailField
from functools import wraps