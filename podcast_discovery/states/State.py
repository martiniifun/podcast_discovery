import reflex as rx


class State(rx.State):
    title:str = "Welcome to Reflex!"
    new_title:str = "Welcome to Podcast-Discovery!"
    old_title:str = "Welcome to Reflex!"

    @rx.event
    def handle_click_event(self) -> None:
        print(self.router.session.client_ip)
        if self.title == self.new_title:
            self.title = self.old_title
        else:
            self.title = self.new_title
