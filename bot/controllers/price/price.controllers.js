import { API } from "$bot/api/index.js";

function getEmojiFlag(value) {
  const code = value.split("_")[1].substring(0, 2);

  return code || "🏳️";
}

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

    const messages = data.map(
      (item) => `:${getEmojiFlag(item.key)}: ${item.title}: ${item.price}`
    );

    await ctx.replyWithMarkdown(messages.join("\n"));
  } catch (error) {
    await ctx.reply(error.message);
  }
};
