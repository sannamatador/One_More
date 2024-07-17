
import time


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode  
        self.time_now = 0

    def __repr__(self):
      return (f"'{self.title}''")

    def __str__(self):
      return (f"{self.title}")

class User:
  def __init__(self, nickname=str, password=str, age=int):
    self.nickname = nickname
    self.password = hash(password)
    self.age = age

  def __repr__(self):
    return (f'{self.nickname }')
  
  def __str__(self):
    return (f'{self.nickname}')
    
class UrTube:
  def __init__(self):
    self.users = []
    self.videos = []
    self.current_user = None

  def __str__(self):
    return (f"{self.current_user}")

  
  def log_in(self, nickname, password):
    for user in self.users:
      if user.nickname == nickname and user.password == hash(password):
        self.current_user = user
    return self.current_user
    
  def log_out(self):
    self.current_user = None

  def register(self, nickname, password, age):
    for user in self.users:
      if user.nickname == nickname:
        print(f"Пользователь {nickname} уже существует")
        return
    self.users.append(User(nickname, password, age)) 
    self.log_in(nickname, password)
    return self.users

       
  def add (self, *video):
    for video in video:
      if video not in self.videos:
        self.videos.append(video)
    return self.videos
      
     
  def get_videos(self, word):
    result = []
    word = word.lower()
    for video in self.videos:
      video.title1 = video.title.lower()
      if word in video.title1:
        result.append(video)
    return result


  def watch_video(self, video):
    if not self.current_user:
        print("Войдите в аккаунт, чтобы смотреть видео")
        return
    for vid in self.videos:
        if vid.title == video:
            if vid.adult_mode and self.current_user.age < 18:
                print("Вам нет 18 лет, пожалуйста, покиньте страницу")
                return
            print("Начало воспроизведения видео")
            for i in range(vid.duration):
                self.current_user.time_now = i
                print(i + 1, end=" ")
                time.sleep(1)
            print("Конец видео")
            self.current_user.time_now = 0
            return
    print("Видео не найдено")



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

#Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')



