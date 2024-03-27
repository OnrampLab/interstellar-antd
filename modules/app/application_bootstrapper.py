from transstellar.framework import Application


class ApplicationBootstrapper:
    def create_app(self, request, testrun_uid):
        application = Application(request, testrun_uid)

        return application
