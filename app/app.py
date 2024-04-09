# DaDFiR3 - DeFi Shiny App

# Load libraries
from shiny import App, render, reactive, ui
from numpy import random
from functools import partial
import matplotlib.pyplot as plt
import pandas as pd
from shiny import App, ui
from extract import load_transactions, load_latest, plot_balance, plot_actus, get_time, get_transactions, set_infura, call_actus

# Global variables TODO - Needed?
LATEST = 18900000
#DEMO_ADDRESSES = "0x46e84ddb17aa374f623d3d843a641bb84436b4e9 , 0xd92E172699fD90b5760585dE4fb3Fb59Ce343985" # small accounts
DEMO_ADDRESSES = "0xF977814e90dA44bFA03b6295A0616a897441aceC, 0xcEe284F754E854890e311e3280b767F80797180d" # top accounts
STATIC_SELECT_DICT = {"A": "All addresses"}
SELECT_DICT = STATIC_SELECT_DICT

# Configuration page => Enter infura id and max transactions to be loaded as a safety abord and ACTUS server URL 
config_ui = ui.page_fluid(
    ui.h2("Configuration"),
    "You have to first set your Infura ID in order to be able to retrieve data from the Ethereum blockchain.",
    # Infura ID
    ui.HTML("<br>Use the following link to get your ID: <a href='https://app.infura.io/'>INFURA</a><br><br> "),
    ui.input_text("infura_id", "Infura ID", "insert your Infura ID"),
    # Max transactions per account to be loaded
    ui.input_text("max_transactions", "Maximum transactions to load", "50"),
    # ACTUS server
    ui.input_text("actus_server", "ACTUS Server URL", "http://localhost:8080"),
    ui.HTML("<br><br>"),
    ui.input_action_button("save_infura", "save"),
    ui.output_text("save"),
)

# Load Data page => select a time range and addresses to be loaded.
load_ui = ui.page_sidebar(  
    ui.sidebar( 
        ui.h2("Load Data"), 
        # ETH addresses (multiple addresses are comma separated)
        ui.input_text_area("eth_address", "Ethereum Address(es) - Multiple => comma separated", DEMO_ADDRESSES),
        # lower bound of blocks
        ui.input_numeric("fromblock", "From Block", 18850000, min=1, max=LATEST),
        ui.output_text("fromtime"), # time for this block is calculated
        # upper bound of blocks
        #ui.input_numeric("toblock", "To Block", 18900000, min=1, max=LATEST),
        #  LATEST gives the last block 
        ui.input_numeric("toblock", "To Block", LATEST, min=1, max=LATEST),
        ui.output_text("totime"), # time for this block is calculated
        "latest block",
        ui.output_text("latest"), # latest block
        # select a protocol. This is needed for the ABI and is retrieved from the param.json
        ui.input_select(  
            "protocol",  
            "Select a protocol:",  
            {"Tether": "Tether", "UniswapLiq": "Uniswap V2 Liquidity"},  
        ), 
        ui.input_action_button("load_data", "load"),
        ui.output_text("load"),
    ),  
    # right side of the page
    # select the account if multiple 
    ui.input_select(  
        "selectaccount",  
        "Select an option below:",  
        SELECT_DICT,
    ),
    # Account information
    ui.output_text("account"),
    ui.output_text("initial_balance"),
    ui.output_text("actual_balance"),
    ui.output_text("total_supply_protocol"),

    ui.output_plot("myplot"),
    ui.output_data_frame("transactions_df"),  
)  


actus_ui = ui.page_sidebar(  
    ui.sidebar(
        ui.h2("ACTUS analysis"),
        #ui.input_switch("auto_update", "Auto update", False),
        ui.input_action_button("actus", "update"),
        ui.output_text("update"),
        #ui.input_radio_buttons(  
        #    "actus_view",  
        #    "ACTUS view",  
        #    {"RPA": "User (RPA)", "RPL": "Bank (RPL)"},  
        #),
    ),
    "ACTUS Output",
    ui.output_plot("actus_plot"),
    ui.output_data_frame("transactions_actus"), 
)


dd_ui = ui.page_fluid(
    "Display",
    #ui.input_action_button("read_data", "read"),
    ui.output_text("data"),
)

navbar_ui = ui.page_navbar(  
    ui.nav_panel("Configuration", config_ui),  
    ui.nav_panel("Load data", load_ui),  
    ui.nav_panel("ACTUS analysis", actus_ui),  
    title="DaDFiR3 DeFi",  
    id="page",  
)  


app_ui = ui.page_fluid(
    navbar_ui,
)


def server(input, output, session):

    #INFURA_PROJECT_ID = reactive.value("")
    ETHEREUM_ADDRESSES = reactive.value([])
    actual_address = reactive.value("empty")
    initial_balance_full = reactive.value(0)
    actual_balance_full = reactive.value(0)
    deposit_data = reactive.value([])
    symbol = reactive.value("US")
    decimals = reactive.value(8)
    total_supply = reactive.value(0)
    CONTRACT = reactive.value("UMP")
    index = reactive.value(0)
    alltransactions = reactive.value([])
    actus_data = reactive.value([])

    @render.text
    def account():
        if input.selectaccount() == "A":
            # all accounts => sum
            all_transactions = alltransactions.get()
            actual_address.set("all")
            help_initial_balance_full = 0
            help_actual_balance_full = 0
            help_deposit_data = []
            for transaction in all_transactions:
                help_initial_balance_full = help_initial_balance_full + transaction[0]
                help_actual_balance_full = help_actual_balance_full + transaction[1]
                help_deposit_data = help_deposit_data + transaction[2]
            initial_balance_full.set(help_initial_balance_full)
            actual_balance_full.set(help_actual_balance_full)
            deposit_data.set(help_deposit_data)
            print(actual_balance_full.get(), decimals.get())
            print(f"Deposits: {deposit_data.get()}")
            return (f"All addresses")
        else:   
            index.set(int(input.selectaccount()))
            i = index.get()
            address =  ETHEREUM_ADDRESSES.get()
            if 0 <= i < len(address):
                all_transactions = alltransactions.get()
                actual_address.set(address[i])
                initial_balance_full.set(all_transactions[i][0])
                actual_balance_full.set( all_transactions[i][1])
                deposit_data.set( all_transactions[i][2])
                #symbol.set(all_transactions[i][3])
                #decimals.set(all_transactions[i][4])
                #CONTRACT.set(all_transactions[i][5])
                print(actual_balance_full.get(), decimals.get())
                return (f"Selected address: {address[i]}")
            else:
                # Return an empty string if the index is out of bounds
                return "No data loaded"

    @render.text
    def initial_balance():
        return (f"Initial balance: {initial_balance_full.get():,.2f} {symbol.get()}")
    
    @render.text
    def actual_balance():
        return (f"Actual balance: {actual_balance_full.get():,.2f} {symbol.get()}")

    @render.text
    def total_supply_protocol():
        return (f"Total supply for {input.protocol()}: {total_supply.get():,.2f} {symbol.get()}")

    @render.text
    def fromtime():     
        return get_time(input.fromblock())

    @render.text
    def totime():
        return get_time(input.toblock())
    
    @render.text
    @reactive.event(input.save_infura)
    def latest():
        return load_latest()

    # TODO - not jet used
    @render.text
    def transactioncount():
        tokens = input.eth_address().split(',')
        # strip whitespace from each token
        tokens = [token.strip() for token in tokens]
        ETHEREUM_ADDRESSES.set(tokens)
        address = ETHEREUM_ADDRESSES.get()
        return get_transactions(address[0],input.fromblock(),input.toblock())

    @render.text
    @reactive.event(input.save_infura)
    def save():
        set_infura(input.infura_id(), input.max_transactions(), input.actus_server())
        str = "Infura ID set to: " + input.infura_id()
        LATEST = load_latest()
        return str
        
    @render.text
    #@reactive.event(input.save_infura)
    def data():
        return actual_balance_full.get()
    
    @render.text()
    @reactive.event(input.load_data)
    def load():
        all_transactions = []
        tokens = input.eth_address().split(',')
        # strip whitespace from each token
        tokens = [token.strip() for token in tokens]
        ETHEREUM_ADDRESSES.set(tokens)
        print(ETHEREUM_ADDRESSES)
        FROM = input.fromblock()
        TO = input.toblock()
        PROTOCOL = input.protocol()
        #initial_balance_full, actual_balance_full, deposit_data, symbol, decimals, total_supply, CONTRACT 
        address = ETHEREUM_ADDRESSES.get()
        for i in range(len(tokens)):  
            transactions = load_transactions(address[i], FROM, TO, PROTOCOL)
            all_transactions.append(transactions)       
        initial_balance_full.set(all_transactions[0][0])
        actual_balance_full.set( all_transactions[0][1])
        deposit_data.set( all_transactions[0][2])
        symbol.set(all_transactions[0][3])
        decimals.set(all_transactions[0][4])
        total_supply.set(all_transactions[0][5])
        CONTRACT.set(all_transactions[0][6])
        alltransactions.set(all_transactions)
        print(actual_balance_full.get(), decimals.get())
        for i, help_address in enumerate(address):
            SELECT_DICT[str(i)] = help_address
        print(f"Select {SELECT_DICT}")
        ui.update_selectize("selectaccount", choices=SELECT_DICT)
        return ""

    @render.text()
    @reactive.event(input.actus)
    def update():
        #address, initial_balance_full, actual_balance_full, deposit_data, symbol, decimals, actus_contract
        actus_df = call_actus(actual_address.get(), initial_balance_full.get(), actual_balance_full.get(), deposit_data.get(), symbol.get(), decimals.get(), CONTRACT.get())
        print(f"From ACTUS SERVER:\n {actus_df}")
        actus_data.set(actus_df)
        return "updated"

    @render.plot(alt="balance sheet")  
    def myplot():  
        fig, ax = plot_balance(initial_balance_full.get(), deposit_data.get(), decimals.get())
        #return fig  

  
    @render.data_frame
    def transactions_df():
        df = pd.DataFrame(deposit_data.get(), columns=['Time', 'Amount'])
        #df['Amount'] = df['Amount'] / (10 ** decimals.get())
        df['Amount'] = (df['Amount']/ (10 ** decimals.get())).apply(lambda x: f"{x:,.2f} {symbol.get()}")
        print(df)
        return render.DataTable(df, width="600px")


    @render.plot(alt="actus sheet")  
    def actus_plot():  
        df = pd.DataFrame(actus_data.get(), columns=['type', 'time', 'payoff', 'nominalValue'])
        fig, ax = plot_actus(df)
        #return fig  

    @render.data_frame
    def transactions_actus():
        df = pd.DataFrame(actus_data.get(), columns=['type', 'time', 'payoff', 'nominalValue'])
        df['payoff'] = (df['payoff']).apply(lambda x: f"{x:,.2f} {symbol.get()}")
        df['nominalValue'] = (df['nominalValue']).apply(lambda x: f"{x:,.2f} {symbol.get()}")
        df = df.rename(columns={'type': 'Type', 'time': 'Time', 'payoff': 'Payoff', 'nominalValue': 'Balance'})
        print(df)
        return render.DataTable(df, width="600px")
    



    #def load():
    #    ETHEREUM_ADDRESS = input.eth_address()
    #    FROM = input.block_range()[0]
    #    TO = input.block_range()[1]
    #    PROTOCOL = input.protocol()
    #    
    #    return f"{ETHEREUM_ADDRESS} {FROM} {TO} {INFURA_PROJECT_ID}"
    

app = App(app_ui, server)
