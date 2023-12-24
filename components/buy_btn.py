# Importing Libraries
import streamlit as st
from bot.bot import Bot
from playwright.sync_api import sync_playwright, TimeoutError

class BuyButtonUI:
    def __init__(self) -> None:

        self.buy_btn = st.button(
            "Start Supremebot",
            key="buy-btn",
            type="primary",
            use_container_width=True)
        if self.buy_btn:

            # Creating the Bot
            bot: Bot = Bot()

            # Start the automation
            bot.scrape()

            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False)
                page = browser.new_page()

                bot.add_to_basket(page)

                try:
                    bot.checkout(page)
                except TimeoutError:
                    pass

                input()
