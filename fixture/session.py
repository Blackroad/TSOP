class SessionHelper:
    def __init__(self, app):
        self.app = app

    # def login(self, username, password):
    #     #login to main dashboard
    #     wd = self.app.wd
    #     self.app.open_home_page()
    #     wd.find_element_by_name("user").clear()
    #     wd.find_element_by_name("user").send_keys(username)
    #     wd.find_element_by_name("pass").clear()
    #     wd.find_element_by_name("pass").send_keys(password)
    #     wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()


