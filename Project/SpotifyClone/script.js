console.log("Welcome to Chord Beats");
let songindex = 0;
let masterprevius = document.getElementById('previous');
let masterPlay = document.getElementById('masterplay')
let myProgressbar = document.getElementById('progressbar');
let gif = document.getElementById('gif');
let songitems = Array.from(document.getElementsByClassName('songitem'));
let songs = [
    {songName:"Akatsuki no Kuruma" , filepath:"songs/Akatsuki no Kuruma.mp3",coverpath:"covers/ak.png" },
    {songName:"Anime Janai" , filepath:"songs/Anime Janai ～ Yume wo Wasureta Furui Chikyujin-yo.mp3",coverpath:"covers/animj.png" },
    {songName:"Believe" , filepath:"songs/Believe.mp3",coverpath:"covers/bel.png" },
    {songName:"Blazing" , filepath:"songs/Blazing.mp3",coverpath:"covers/blaze.png" },
    {songName:"Dreams" , filepath:"songs/Dreams.mp3",coverpath:"covers/dreams.png" },
    {songName:"EARth" , filepath:"songs/EARth.mp3",coverpath:"covers/earth.png" },
    {songName:"G" , filepath:"songs/G.mp3",coverpath:"covers/g.png" }

];


//printing the song item on the list
songitems.forEach((element, i)=>{
    console.log(element , i);
    element.getElementsByTagName("img")[0].src = songs[i].coverpath;
    element.getElementsByClassName("songname")[0].innerText = songs[i].songName;


}); 
let audioelement = new  Audio('songs/Akatsuki no Kuruma.mp3');
//audioelement.play()


//handling play /pause

masterPlay.addEventListener('click' , ()=>{
    if(audioelement.paused || audioelement.currentTime<= 0){
        audioelement.play();
        masterPlay.classList.remove('fa-circle-play');
        masterPlay.classList.add('fa-circle-pause');
        gif.style.opacity = 1;

    }
    else{
        audioelement.pause();
        masterPlay.classList.remove('fa-circle-pause');
        masterPlay.classList.add('fa-circle-play');
        gif.style.opacity = 0;
    }
})

//Listen to events 

audioelement.addEventListener('timeupdate' , ()=>{
   
    progress = parseInt((audioelement.currentTime/audioelement.duration)*100)
    //console.log(audioelement.currentTime)
    
    myProgressbar.value = progress
})


//handling click on progressbar
myProgressbar.addEventListener('change' , ()=>{
    audioelement.currentTime = myProgressbar.value* audioelement.duration /100;

})


//play button on the list


const makeAllPlays = ()=>{
    
    Array.from(document.getElementsByClassName('songItemPlay')).forEach((element)=>{
        element.classList.remove('fa-pause-circle');
        element.classList.add('fa-play-circle');
    })
}
Array.from(document.getElementsByClassName('songItemPlay')) .forEach((element)=>{
    element.addEventListener('click' , (e)=>{
        console.log(e);
        makeAllPlays();
        songindex = parseInt(e.target.id);
        console.log(songindex); 
        e.target.classList.remove('fa-circle-play');
        e.target.classList.add('fa-circle-pause');
        audioelement.currentTime = 0;
        src = songs[--songindex].filepath
        audioelement.src=src;
        audioelement.play();
        masterPlay.classList.remove('fa-circle-play');
        masterPlay.classList.add('fa-circle-pause');
    });

})

//previous and next buttons

document.getElementById('next').addEventListener('click' , ()=>{
    if(songindex > 9){
        songindex = 0;
    }
    else{
        songindex+=1;
    }
    audioelement.currentTime = 0;
    src = songs[songindex].filepath
    audioelement.src=src;
    audioelement.play();
    masterPlay.classList.remove('fa-circle-play');
    masterPlay.classList.add('fa-circle-pause');
    

});
document.getElementById('previous').addEventListener('click' , ()=>{
    if(songindex < 1){
        songindex = 0;
    }
    else{
        songindex-=1;
    }
    audioelement.currentTime = 0;
    src = songs[songindex].filepath
    audioelement.src=src;
    audioelement.play();
    masterPlay.classList.remove('fa-circle-play');
    masterPlay.classList.add('fa-circle-pause');
    

});
