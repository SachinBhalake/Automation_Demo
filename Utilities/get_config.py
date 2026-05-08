import yaml


class ConfigReader:

    _config = None

    def __init__(self, env, headless, sel_browser, plw_browser, plw_slowmo):

        # -------- Config YAML --------
        if ConfigReader._config is None:
            with open("Config/config.yaml", encoding="utf-8") as file:
                ConfigReader._config = yaml.safe_load(file)

        self.config = ConfigReader._config
        self.environments = self.config.get("environments", {})

        self.env = env
        self.headless = headless
        self.sel_browser = sel_browser
        self.plw_browser = plw_browser
        self.plw_slowmo = plw_slowmo

    # -------- getters --------
    def get_env(self):
        return self.env

    def get_sel_browser(self):
        return self.sel_browser

    def get_plw_browser(self):
        return self.plw_browser

    def is_headless(self):
        return self.headless

    def get_slowmo(self):
        return self.plw_slowmo

    def get_grid_url(self):
        return self.config.get("selenium_grid_url")

    def get_ui_base_url(self):
        return self.environments[self.env]["ui_base_url"]

    def get_api_base_url(self):
        return self.environments[self.env]["api_base_url"]
