import Pyro4

ticket = 0

@Pyro4.expose

class GenerateTicket(object):
    def say_generate(self, name):
          return "Hello {0}".format(name)

    def new_ticket(self):
        global ticket
        ticket += 1
        return "Ticket {0}".format(ticket)

daemon = Pyro4.Daemon()
uri = daemon.register(GenerateTicket)

print("Ready. Object uri =", uri)
daemon.requestLoop()