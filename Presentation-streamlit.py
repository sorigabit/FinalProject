###############################
# This program lets you       #
# - Create a dashboard        #
# - Evevry dashboard page is  #
# created in a separate file  #
# ##############################

import streamlit as st
from PIL import Image
from poate import poate
import pandas as pd
import numpy as np
from time import sleep
from random import randint
from bs4 import BeautifulSoup
import requests
import re
import ast
from requests import get
from dateutil.parser import parse
from urllib.request import urlopen as uReq
import json
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.stem import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
from termcolor import colored


st.set_page_config(layout="wide")
def main():
 


    options = ['Home','Early days','Golden age','60s to 2000', 'Our days', 'Recommender']
    choice = st.sidebar.selectbox("Menu",options, key = '1')

    if ( choice == 'Home' ):
#       st.title(":blue[Movies], a neverending story!")
      
      image = Image.open(r'C:\Users\sorig\Desktop\Streamlit Project\images\intro23.jpg')
      st.image(image, width=1100)
      pass

    elif ( choice == 'Early days' ):
      st.title("WHO INVENTED CINEMA?")
      st.title("\n\n\n\n")  
      st.title("\n\n\n\n") 
      st.title("\n\n\n\n")
      col1, padding, col2 = st.columns((15,1,10))
      with col1:
        st.write("In June 1889, American inventor Thomas Edison assigned a \n lab assistant, William Kennedy Dickson, to help develop a\n  device that could produce visuals to accompany the sounds produced from the phonograph.So, the Edison Company successfully demonstrated a prototype of the Kinetoscope, which enabled one person at a time to view moving pictures. The first public Kinetoscope demonstration took place in 1893. By 1894 the Kinetoscope was a commercial success, with public parlours established around the world.\n ")
        st.title("\n\n\n\n") 
        st.title("\n\n\n\n") 
        st.title("\n\n\n\n") 
        st.title("\n\n\n\n") 
        st.title("\n\n\n\n") 
        st.title("\n\n\n\n") 
        st.title("WHAT WERE EARLY FILMS LIKE?")
        st.write("At first, films were very short, sometimes only a few minutes or less. They were shown at fairgrounds, music halls, or anywhere a screen could be set up and a room darkened. Subjects included local scenes and activities, views of foreign lands, short comedies and newsworthy events.\n By 1914, several national film industries were established. At this time, Europe, Russia and Scandinavia were the dominant industries; America was much less important. Films became longer and storytelling, or narrative, became the dominant form.\nThe first feature-length movie incorporating synchronised dialogue, The Jazz Singer (USA, 1927).")
        st.title("\n\n\n\n\n\n\n\n\n\n")
        st.title("\n\n\n\n\n\n\n\n\n\n")
        st.title("\n\n\n\n\n\n\n\n\n\n")
        st.title("\n\n\n\n\n\n\n\n\n\n")
        st.title("\n\n\n\n\n\n\n\n\n\n")
        st.title("\n\n\n\n\n\n\n\n\n\n")
        st.title("\n\n\n\n\n\n\n\n\n\n")
        st.image(r'./images/musicals.jpg')
      with col2:
        image = Image.open(r'C:\Users\sorig\Desktop\Streamlit Project\images\kineto.jpg')
        st.image(image)
        st.title("\n\n")    
        image1 = Image.open(r'C:\Users\sorig\Desktop\Streamlit Project\images\old.jpeg')
        st.image(image1)
      pass

    elif ( choice == 'Golden age' ):
      st.title("CINEMA’S GOLDEN AGE")
      image = Image.open(r'C:\Users\sorig\Desktop\Streamlit Project\images\goldenage.jpg')
      st.image(image)
      st.write('By the early 1930s, nearly all feature-length movies were presented with synchronised sound and, by the mid-1930s, some were in full colour too. The advent of sound secured the dominant role of the American industry and gave rise to the so-called ‘Golden Age of Hollywood’.During the 1930s and 1940s, cinema was the principal form of popular entertainment, with people often attending cinemas twice a week. Ornate ’super’ cinemas or ‘picture palaces’, offering extra facilities such as cafés and ballrooms, came to towns and cities; many of them could hold over 3,000 people in a single auditorium.In Britain, the highest attendances occurred in 1946, with over 31 million visits to the cinema each week.The introduction of television in America prompted a number of technical experiments designed to maintain public interest in cinema. Even so, While cinemas had some success in fighting the competition of television, they never regained the position and influence they held in the 1930s and 40s, and over the next 30 years audiences dwindled. By 1984 cinema attendances in Britain had declined to one million a week.')
      image2 = Image.open(r'C:\Users\sorig\Desktop\Streamlit Project\images\uk.jpg')
      st.image(image2)
      image1 = Image.open(r'C:\Users\sorig\Desktop\Streamlit Project\images\us1.jpg')
      st.image(image1)
      pass
    
    elif ( choice == '60s to 2000' ):
        col1, padding, col2 = st.columns((15,1,10))
        with col1:
            st.title("Youth Culture of the 1960s and 1970s")
            st.write("During the 1960s and 1970s, there was a rise in films—including Bonnie and Clyde, The Wild Bunch, 2001: A Space Odyssey, and Easy Rider—that celebrated the emerging youth culture and a rejection of the conservatism of the previous decades. This also led to looser attitudes toward depictions of sexuality and violence in film.")
            st.title("\n\n\n\n\n\n\n\n\n\n")
            st.title("\n\n\n\n\n\n\n\n\n\n")
            st.title("\n\n\n\n\n\n\n\n\n\n")
            st.title("\n\n\n\n\n\n\n\n\n\n")
            st.title("\n\n\n\n\n\n\n\n\n\n")
            st.title("\n\n\n\n\n\n\n\n\n\n")
            st.title("Blockbusters and the VCR")
            st.write("The 1970s and 1980s saw the rise of the blockbuster, with films like Jaws, Star Wars, Raiders of the Lost Ark, and The Godfather. The adoption of the VCR by most households in the 1980s reduced audiences at movie theaters but opened a new mass market of home movie viewers. Improvements in computer animation led to more special effects in film during the 1990s with movies like The Matrix, Jurassic Park, and the first fully computer-animated film, Toy Story.")
        with col2:
            st.title("\n\n\n\n\n\n\n\n\n\n")
            st.image(r'./images/space.jpg')
            st.title("\n\n\n\n\n\n\n\n\n\n")
            st.title("\n\n\n\n\n\n\n\n\n\n")
            st.image(r'./images/toystory.jpg')
            
        pass
    
    elif ( choice == 'Our days' ):
          st.title("The film industry today")
          st.image(r'./images/poster.jpg')
          st.write("The concept of streaming media has been around for several decades, but it was only in the early 2000s that the technology started to take off. The first streaming services were mostly focused on delivering music and other audio content, but as internet speeds improved, video streaming became more viable.Today, there are numerous streaming services available, each with their own unique features and limitations. From Netflix to Hulu to HBO Max, streaming has become an essential part of how we consume media. The convenience of streaming has made it an attractive alternative to traditional cable TV, and it has had a significant impact on the film industry")
          st.write("Streaming services have changed the film industry in numerous ways. One of the biggest changes is in the way films are financed and produced. With the rise of independent production companies, filmmakers now have more opportunities to secure funding for their projects. Streaming services have also given filmmakers more creative control, as they are not beholden to the demands of traditional studios")
          st.write("Streaming services have also changed the way films are distributed. The traditional theatrical release model has been disrupted, with many films now premiering exclusively on streaming platforms. This has given filmmakers more options for distribution. It’s also opened up new audiences to films that might not have received a theatrical release.")
          st.write(":blue[•Netflix currently has 209.18 million subscribers. Up from only 24.30 million subscribers in 2011.]")
          st.write(":blue[•Netflix generated 24.99 billion american dollars in 2020. As of June 2021, Netflix has generated 14.5 billion american dollars in revenue so far in 2021.]")
          st.write(":blue[•Netflix has 5,800 content titles in their US library.]")
          st.write(":blue[•64.65% of Netflix subscribers are based outside of the US & Canada.]")
          st.write(":blue[•In 2020, 80% of the most watched original series in the US belonged to Netflix.]")
          st.write(":blue[•Netflix subscribers spend an average of 3.2 hours per day watching content on the platform.]")
          st.write(":blue[•Netflix’s mobile app for iOS & Android was downloaded 16.4 million times in June 2021 alone.]")
          image = Image.open(r'C:\Users\sorig\Desktop\Streamlit Project\images\net.jpg')
          st.image(image)
          st.write("In 2022, USA produced more than 1000 movies with top grossing movie being Avatar The way of water.France produced 396 movies and their top grossing movie was Triangle of Sadness. Some other intereseting fact about today's movie industry is that Bollywood is a 3 Billion american dollars business. China's cinema industry is 4 times that number and Hollywood is 17 times")
          
          image = Image.open(r'C:\Users\sorig\Desktop\Streamlit Project\images\nrmov.jpg')
          st.image(image)


          pass
    
    elif ( choice == 'Recommender' ):
           st.title("What should i watch?")
           st.subheader(":red[The average American watches roughly four hours of movies or television each day, and they spend another hour looking for something to watch.]")
           col1, padding, col2 = st.columns((15,1,10))
           with col1:
                st.image(r'./images/search.jpg')
                st.title("\n\n\n\n\n\n\n\n\n\n")
                st.title("\n\n\n\n\n\n\n\n\n\n")
                st.title("\n\n\n\n\n\n\n\n\n\n")
                st.title("\n\n\n\n\n\n\n\n\n\n")
                st.title("\n\n\n\n\n\n\n\n\n\n")
                st.title("\n\n\n\n\n\n\n\n\n\n")
                st.title("\n\n\n\n\n\n\n\n\n\n")
                st.title("\n\n\n\n\n\n\n\n\n\n")
                st.image(r'./images/votes.jpg')
                st.image(r'./images/time.jpg')
                st.image(r'./images/wordcloud.png')
                st.title("\n\n\n\n\n\n\n\n\n\n")
                st.title("\n\n\n\n\n\n\n\n\n\n")
                st.title("\n\n\n\n\n\n\n\n\n\n")
                st.title("\n\n\n\n\n\n\n\n\n\n")
                st.image(r'./images/recom.jpg')
                st.title("\n\n\n\n\n\n\n\n\n\n")
                st.title("\n\n\n\n\n\n\n\n\n\n")
                st.title("\n\n\n\n\n\n\n\n\n\n")
                st.write("Sources:")
                st.write("https://open.lib.umn.edu/mediaandculture/chapter/8-2-the-history-of-movies/")
                st.write("https://www.blog.thefilmfund.co/the-impact-of-streaming-on-the-film-industry/")
                st.write("https://backlinko.com/netflix-users")


                
                
           with col2:
                st.title("\n\n\n\n\n\n\n\n\n\n")
               
                
                st.write("So you are finally home after a long day at work and you decide to relax by watching a movie.You open your tv, your favourite streaming service and you scroll through some options and watch a trailer. It is nice, but maybe a different movie would be better. So you search for another one and watch another trailer, then another, and another, and another. Thirty minutes later, you are still watching trailers, still have not picked a movie. It's hard, isn't it?\n")
                st.write("Let's try this recommender, it will give you a list of movies. Some will be close to what you're looking, some of them will not. But hey, at least you're not torturing your tv remote!")
                
                st.write(":blue[A few things about it:]")
                st.write("1.	It is using a database of 5000 movies\n")
                st.write("2.	Features: actors, director, description, keywords, genre\n")
                st.write("3.	 It is using coisine similarity for analysing the text\n")
                st.write("4.	It recommends 5 movies, specifying the release date, the director and the average rating of each one of them")

main()
