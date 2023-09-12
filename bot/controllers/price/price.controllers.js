import { API } from "$bot/api/index.js";

export const GOLD = async (ctx) => {
  try {
    const { data } = await API.get("price/gold");

    const messages = [];

    await Promise.all(
      data.map((item, index) => {
        index !== 0 && messages.push(`\n`);

        messages.push(item.title);

        item.prices.map((price) =>
          messages.push(`${price.title}: ${price.price}`)
        );
      })
    );

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
