from discord.ext import commands, tasks
from datetime import datetime, time as dtime


class auto_msg(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.messages = {
            dtime(12, 34): "Witajcie na Daily Coachingu. Zaczynamy! Jakie macie dzisiaj tematy?",
            dtime(12, 45): "Zostało **15 minut** spotkania.",
            dtime(12, 50): "Zostało nam **10 minut**.",
            dtime(12, 55): "Zaraz będziemy kończyć dzisiejsze spotkanie...",
            dtime(12, 59): "**Kończymy na dziś**. <@404038151565213696>, <@1082683392342114335> i ja, dziękujemy Wam za to spotkanie. Pamiętajcie, że zawsze możecie wrzucić kolejne tematy na agendę, dodając je na stronie [Daily Coaching - tematy](https://apply.siadlak.com/tematy-daily-coaching). Dzięki raz jeszcze i do jutra!",
        }
        self.channel_id = 1120658406160732160
        self.check_time.start()

    @tasks.loop(seconds=60)
    async def check_time(self):

        now = datetime.now().time()
        current_time = dtime(now.hour, now.minute)
        if current_time in self.messages:
            channel = self.bot.get_channel(self.channel_id)
            if channel:
                await channel.send(self.messages[current_time])


def setup(bot: commands.Bot):
    bot.add_cog(auto_msg(bot))