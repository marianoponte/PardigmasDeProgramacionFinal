from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import Required

class ClienteForm(FlaskForm):
    cliente = StringField('Cliente: ', validators=[Required()])
    ingresar = SubmitField('Buscar')

class ProductoForm(FlaskForm):
    producto = StringField('Producto: ', validators=[Required()])
    ingresar = SubmitField('Buscar')

class LoginForm(FlaskForm):
    usuario = StringField('Nombre de usuario', validators=[Required()])
    password = PasswordField('Contraseña', validators=[Required()])
    enviar = SubmitField('Ingresar')

class RegistrarForm(LoginForm):
    password_check = PasswordField('Verificar Contraseña', validators=[Required()])
    enviar = SubmitField('Registrarse')

class CargarVentaForm(FlaskForm):
	codigo = StringField('Código del producto: ', validators=[Required()])
	producto = StringField('Nombre del producto: ', validators=[Required()])
	cliente = StringField('Cliente: ', validators=[Required()])
	cantidad = StringField('Cantidad: ', validators=[Required()])
	precio = StringField('Precio: ', validators=[Required()])
	cargar = SubmitField('Cargar')