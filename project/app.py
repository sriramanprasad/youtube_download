import streamlit as st
from pytube import YouTube
import tempfile

st.set_page_config(
    page_title="Youtube Downloader",
    page_icon="./logo_nphi.png",
    layout="wide",
    initial_sidebar_state="expanded",
    

)


st.markdown("<h1 style='text-align: center; color: red; font-style:italic;'>NΦ UTube downloader</h1>", unsafe_allow_html=True)
st.markdown(
        """
        <div class="footer">
            Made with ❤️ by <a href="https://www.linkedin.com/in/sourav-bera-85a184218/" target="_blank">Sourav</a>
        </div>

        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            background-color: #f8f9fa;
            color: #6c757d;
        }
        </style>
        """,
        unsafe_allow_html=True
    )




link = st.text_input(label="Paste your link here",placeholder="https://www.youtube.com/..")

#function for youtube link is valid or not
def is_youtube(link):
    try:
        yt = YouTube(link)
        return yt.streams.filter(only_video=True).first() is not None
    except:
        return False

#function for key serach of a dictionary
def key_search(dicti , value):
  return list(filter(lambda x: dicti[x] == value, dicti))[0]



if (is_youtube(link)):
    youtube_1=YouTube(link)
    title=youtube_1.title
    st.write(title)
    st.image(youtube_1.thumbnail_url , width=200 )
    out = st.selectbox("Select format" , ('Audio','Video'))
   

    #now for audio
    if out == "Audio":
        audio = youtube_1.streams.filter(only_audio=True)
        #print(list(audio))
        list_aud = {}
        for i in range(len(audio)):
            list_aud[i] = audio[i].abr
        strm = st.selectbox("Select Quality",(list_aud.values()))
        
        key_val = key_search(list_aud,strm)
        temp_dir = tempfile.mkdtemp()
        temp_file_path = temp_dir + f"/{title}.mp3"
        #print(temp_dir)
        if audio[key_val].download(output_path=temp_dir,filename=f'{title}.mp3'):#output_path=temp_dir,filename='audio')
        #st.download_button(label="Download" , data=file,file_name=audio.mp3)
            st.download_button(
                label = "download",
                data = open(temp_file_path,'rb').read(),
                file_name=f'nphi-{title}.mp3',
                mime='audio/mp3'
            )
        
    elif out=="Video":
        video = [stream for stream in youtube_1.streams if stream.includes_audio_track and stream.includes_video_track]

        list_vid = {}
        for i in range(len(video)):  
            list_vid[i] = video[i].resolution
            #print(video[i])
        
           

        #print(list_vid)
        strm = st.selectbox("Select Quality",(list_vid.values()))
        key_val = key_search(list_vid,strm)
        #print(video[key_val])
        extension=video[key_val].mime_type.split('/')[1]

        
        
        temp_dir = tempfile.mkdtemp()
        temp_file_path = temp_dir + f"/{title}.{extension}"
        
        if video[key_val].download(output_path=temp_dir,filename=f'{title}.{extension}'):#output_path=temp_dir,filename='audio')
        
            st.download_button(
                label = "download",
                data = open(temp_file_path,'rb').read(),
                file_name=f'nphi-{title}.{extension}',
                mime='video/mp4'
            )
            


else:
    st.write("Please Enter a Valid Link")


