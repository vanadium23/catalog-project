from app.models import User, Category, Item
from app.database import db_session

# It is file for seeding database with first values
newUser = User(name='vanadium23',
               email='chernoffivan@gmail.com',
               picture='')
db_session.add(newUser)
db_session.commit()
user = User.query.filter_by(email='chernoffivan@gmail.com').one()

comedy = Category('Comedy',
                  '''
                  There are a very funny films
                  ''',
                  user.id)
db_session.add(comedy)
db_session.commit()
comedy = Category.query.filter_by(name='Comedy').one()

animation = Category('Animation',
                     '''
                     There are a animated films for kid
                     ''',
                     user.id)
db_session.add(animation)
db_session.commit()
animation = Category.query.filter_by(name='Animation').one()


sci_fi = Category('Sci-Fi',
                  '''
                  There are a films in Sci-Fi genre
                  ''',
                  user.id)
db_session.add(sci_fi)
db_session.commit()
sci_fi = Category.query.filter_by(name='Sci-Fi').one()


pitch = Item('Pitch Perfect 2',
             '''
             After a humiliating command performance
             at Lincoln Center, the Barden Bellas
             enter an international competition
             that no American group has ever won
             in order to regain their status
             and right to perform.
             ''',
             comedy.id,
             user.id)
pitch.image_name = 'pitch_perfect_2.jpg'
db_session.add(pitch)
db_session.commit()

home = Item('Home',
            '''
            Oh, an alien on the run from his own people,
            lands on Earth and makes friends
            with the adventurous Tip,
            who is on a quest of her own.
            ''',
            animation.id,
            user.id)
home.image_name = 'home.jpg'
db_session.add(home)
db_session.commit()

mad_max = Item('Mad Max: Fury Road',
               '''
               In a stark desert landscape where humanity is broken,
               two rebels just might be able to restore order:
               Max, a man of action and of few words, and Furiosa,
               a woman of action who is looking to make it back
               to her childhood homeland.
               ''',
               sci_fi.id,
               user.id)
mad_max.image_name = 'mad_max.jpg'
db_session.add(mad_max)
db_session.commit()
