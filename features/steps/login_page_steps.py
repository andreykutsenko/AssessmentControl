from behave import given, when, then

@given('Open login page')
def open_page(context):
    context.app.login_page.open_login()

@when('Filling {login} and {password} fields')
def filling_field(context, login, password):
    context.app.login_page.filling_login_fields(login, password)

@when('Filling {email} field')
def filling_email_field(context, email):
    context.app.login_page.filling_email_field(email)

@when('Click Sign In button')
def click_signin(context):
    context.app.login_page.click_signin_button()

@when('Click Register Now link')
def click_reg_now(context):
    context.app.login_page.click_register_now()

@when('Click Register Me button')
def click_reg_me(context):
    context.app.login_page.click_register_me()

@when('Filling registration form')
def filling_form(context):
    context.app.login_page.filling_fields(context)

@when('Click I forgot my password')
def click_fogot_my_password(context):
    context.app.login_page.click_fogot_password()

@when('Click Request Password Reset')
def click_reset_password_button(context):
    context.app.login_page.click_password_reset()