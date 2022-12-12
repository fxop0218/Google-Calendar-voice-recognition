from datetime import datetime, timedelta
from quickstart import get_calendar_service
import assistant
import time


def take_title():
    assistant.talk("¿Cuál es el título del nuevo evento?")
    title = assistant.listen()
    return title


def take_description():
    assistant.talk("¿Cuál es la descripción del evento?")
    title = assistant.listen()
    return title


def take_start_data():
    assistant.talk("¿Cuál es la fecha y la hora a la que empieza el evento?")
    # 31 del 12 del 2021 a las 5:30
    date_and_time = assistant.listen().replace("a las", "del").replace("el", "")
    # date_and_time = 31 del 12 del 2021 del 5:30
    date_and_time = date_and_time.split("d")
    print(date_and_time)
    # date_and_time = ["31","12","2021","4:30"]
    date = f"{date_and_time[2]}-{date_and_time[1]}-{date_and_time[0]} {date_and_time[3]}"
    # data = 2021-12-31 5:30
    # Transform into ISO fromat
    return datetime.fromisoformat(date).isoformat()


def take_end_data():
    assistant.talk("¿Cuál es la fecha y la hora del fin del evento?")
    # 31 del 12 del 2021 a las 5:30
    date_and_time = assistant.listen().replace(" a las ", " del ")
    # date_and_time = 31 del 12 del 2021 del 5:30
    print(date_and_time)
    date_and_time = date_and_time.split(" del ")
    # date_and_time = ["31","12","2021","4:30"]
    date = f"{date_and_time[2]}-{date_and_time[1]}-{date_and_time[0]} {date_and_time[3]}"
    # data = 2021-12-31 5:30
    # Transform into ISO fromat
    return datetime.fromisoformat(date).isoformat()


def create_event():
    event_title = take_title()
    time.sleep(0.5)
    event_desc = take_description()
    time.sleep(0.5)
    event_start = take_start_data()
    time.sleep(0.5)
    event_finsih = take_end_data()

    calendar_serv = get_calendar_service()
    event_res = calendar_serv.events().insert(calendarId="primary",
                                              body={
                                                  "summary": event_title,
                                                  "description": event_desc,
                                                  "start": {"dateTime": event_start, "timeZone": "Europe/Madrid"},
                                                  "end": {"dateTime": event_finsih, "timeZone": "Europe/Madrid"}
                                              }).execute()

    print("Evento creado en exito.")
    assistant.talk(
        f"Se ha creado el evento {event_res['summary']} a las {event_res['start']} y acaba a las {event_res['end']}")


if __name__ == "__main__":
    create_event()
