export const START = async (ctx) => {
  let buttons = [
    [
      {
        text: "طلا",
        callback_data: "gold",
      },
      {
        text: "ارز",
        callback_data: "currency",
      },
    ],
  ];

  const message = "جهت ادامه نوع قیمت را انتخاب کنید:";

  const buttonsMarkup = {
    reply_markup: {
      inline_keyboard: buttons,
    },
  };

  await ctx.reply(message, buttonsMarkup);
};
