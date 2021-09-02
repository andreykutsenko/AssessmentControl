from behave import then

@then('The {username} should be displayed correctly on the page')
def verify_flight(context, username):
    context.app.results_page.verify_username(username)

@then('Verify title "{text}" on confirmation page')
def verify_flight(context, text):
    context.app.results_page.verify_title_page(text)

@then('Verify "{text}" on login page')
def verify_flight(context, text):
    context.app.results_page.verify_text_on_page(text)