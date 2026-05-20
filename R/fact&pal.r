fact<-function(n){
    if(n==1)
        return(1)
    else 
        return(n*fact(n-1))
}

pal<-function(s){
    s=paste(rev(strsplit(s," ")[[1]]),collapse=" ")
}

