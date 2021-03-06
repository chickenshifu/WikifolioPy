
#WikifolioPy imports all submodules and calls them within its own methods. This is to allow a more conventient use of the bot.
from credentials import credentials
from activateSession import SessionActivator
from controlBrowser import BrowserController
from checkWikifolio import CheckWikifolio


class WikifolioPy:
    '''Main class to be instantiated from, all modules are bundled into that class.

    Subsequent methods are implemented and provided by the <modules>:

    login, logout <controlBrowser.py>

    get_cash_amount <checkAccountBalance.py>

    ....


    '''

    def __init__(self, symbol):
        self.symbol = symbol 
        self.credentials = credentials()
        self.s = SessionActivator(self.credentials).activateSession()
        self.session = self.s['session']
        self.connectionToken = self.s['connectionToken']
        self.browserController = BrowserController(self.credentials)
        self.checkWikifolio = CheckWikifolio(self.session, self.symbol)

    def login(self):
        self.browserController.login()

    def logout(self):
        self.browserController.logout()

    def get_portfolio_items(self):
        self.checkWikifolio.get_items()

    def get_cash_amount(self):
        self.checkWikifolio.check_balance() 

    def enter_order(self):
        return None
