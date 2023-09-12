import { Telegraf } from "telegraf";

import { Socks5 } from "$bot/connections/index.js";
import { Price, Bot } from "$bot/controllers/index.js";
// import { id as idMiddleware } from "$bot/middlewares/index.js";
import { botConfig, appConfig } from "$bot/config/index.js";

const bot = new Telegraf(botConfig.token, {
  telegram: {
    agent: !appConfig.published && Socks5,
  },
});

bot.start(Bot.START);

bot.action("gold", Price.GOLD);

export default bot;
