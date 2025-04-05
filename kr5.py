from telegram.ext import Application, ContextTypes
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
import pytz  # Импортируем библиотеку для работы с часовыми поясами

# Конфигурация
BOT_TOKEN = "7436613145:AAFP02KfEzJCRhOMN24RqR9Kjzy9JNjFZa8"  # Замените на токен от @BotFather
CHANNEL_ID = "@test_my_new_phytonik"     # Например, "@my_test_channel"
TIMEZONE = pytz.timezone('Europe/Moscow')  # Укажите ваш часовой пояс

# Асинхронная функция для отправки сообщения
async def send_weekly_message(context: ContextTypes.DEFAULT_TYPE):
    message = "📢 Это еженедельное сообщение от бота!"
    await context.bot.send_message(chat_id=CHANNEL_ID, text=message)

# Запуск бота и планировщика
async def main():
    # Создаем Application с явным указанием JobQueue
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Настраиваем планировщик с указанием часового пояса
    scheduler = AsyncIOScheduler(timezone=TIMEZONE)
    application.job_queue.scheduler = scheduler
    
    # Запускаем периодическую задачу (раз в неделю)
    application.job_queue.run_repeating(
        send_weekly_message,
        interval=604800,  # 7 дней в секундах
        first=10          # Первая отправка через 10 сек (для теста)
    )
    
    print("Бот запущен! Ожидание еженедельной отправки...")
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
