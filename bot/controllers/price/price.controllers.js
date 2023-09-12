import { API } from "$bot/api/index.js";

export const GOLD = async (ctx) => {
  try {
    const { data } = await API.get("price/gold");

    const messages = [JSON.stringify(data)];

    await ctx.replyWithMarkdown(messages.join("\n"));
  } catch (error) {
    await ctx.reply(error.message);
  }
};

export const CURRENCY = async (ctx) => {
  try {
    const { data } = await API.get("price/currency");

    const messages = data.map((item) => `${item.title}: ${item.price}`);

    await ctx.replyWithMarkdown(messages.join("\n"));
  } catch (error) {
    await ctx.reply(error.message);
  }
};
