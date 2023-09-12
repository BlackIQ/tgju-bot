const ids = [6371168857];

const id = async (ctx, next) => {
  const { id } = ctx.message.chat;

  if (ids.includes(id)) {
    next();
  } else {
    const messages = [
      "امکان استفاده از سیستم وجود ندارد.",
      `آیدی چت: \`${id}\``,
    ];

    return await ctx.replyWithMarkdown(messages.join("\n"));
  }
};

export default id;
