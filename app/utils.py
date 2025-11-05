# import os
# from openai import OpenAI
# from sqlalchemy.orm import Session
# from database import SessionLocal
# from crud import update_translation_task, set_task_in_progress, set_task_failed
# from dotenv import load_dotenv


# load_dotenv()

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")


# client = OpenAI(api_key=OPENAI_API_KEY)

# def perform_translation(task_id: int, text: str, languages: list):

#     db = SessionLocal()
#     try:
#         set_task_in_progress(db, task_id)
#         translation = {}

#         for lang in languages:
#             prompt = f"Translate the following text into {lang}:\n\n{text}\n\nReply with only the translation."

#             try:

#                 response = client.chat.completions.create(
#                     model=OPENAI_MODEL,
#                     messages=[
#                         {"role": "user", "content": prompt}
#                     ],
#                     max_tokens=1500,
#                     temperature=0.2
#                 )

#                 translated_text = response.choices[0].message.content.strip()
#                 translation[lang] = translated_text

#             except Exception as e:
#                 print(f"Error translating to {lang}: {e}")
#                 translation[lang] = f"error: {str(e)}"

#         update_translation_task(db, task_id, translation)

#     except Exception as e:
#         print("Unexpected error in perform_translation:", e)
#         set_task_failed(db, task_id, str(e))
#     finally:
#         db.close()


import os
import json
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import update_translation_task, set_task_in_progress, set_task_failed
from deep_translator import GoogleTranslator


def perform_translation(task_id: int, text: str, languages: list):

    db = SessionLocal()
    try:
        set_task_in_progress(db, task_id)
        translation = {}

        for lang in languages:
            try:
                translated_text = GoogleTranslator(
                    source="auto", target=lang
                ).translate(text)
                translation[lang] = translated_text
            except Exception as e:
                print(f"Error translating to {lang}: {e}")
                translation[lang] = f"error: {str(e)}"

        translation_str = json.dumps(translation, ensure_ascii=False)
        update_translation_task(db, task_id, translation_str)

    except Exception as e:
        print("Unexpected error in perform_translation:", e)
        set_task_failed(db, task_id, str(e))
    finally:
        db.close()
