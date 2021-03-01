#
# Calcuration for AP, AD and APH
#------------------------------------------------------------
# beta_0.0  2019/02/19 ay.r and ad_ap.r
# alpha_1.0 2019/04/30 updated 
#
#------------------------------------------------------------
#
#Usage: >Rscript AdApAy.R [-y/pd] ./test/test.csv
#Usage: >Rscript AdApAy.R [-f] ./test/ad/test.csv
#cd/d D:/Dropbox/Dropbox/Study/Ishizaka-labo/IseBay-Photographs/Libraries_for_IseBay/mps
#chcp 65001
#Usage(win): >C:\"Program Files"\R\R-3.5.3\bin\Rscript.exe AdApAy.R -y test\ay\filenamelist.csv
#Usage(win): >C:\"Program Files"\R\R-3.5.3\bin\Rscript.exe AdApAy.R -p test\ap\fnlist_p.csv
#            >C:\"Program Files"\R\R-3.5.3\bin\Rscript.exe AdApAy_ver01.R -f ay/0301/flist.csv
#            >C:\"Program Files"\R\R-3.5.3\bin\Rscript.exe AdApAy_ver01.R -y ay/0301/flist_0301.csv
#You had better to set PATH to "C:\Program Files\R\R-3.5.3\bin\ etc. 
#Arguments
#1st :options
#2nd :file to specify ASC and sampling points etc.
#Options
#> Rscript AdApAy.R -p test/ap/fnlist_p.csv 
# -d: Calculation for ad
# -p: Calculation for ap only
# -ph: Calculation for ah
# -f: Make file of ASC lists in a directry (second argument)
#
#
#------------------------------------------------------------
#changed at 
#-Run from prompt
#-Calculate all spectra (ad/ap/ay) with the script
#-for windows
#------------------------------------------------------------
# libraries
library(ggplot2)
library(reshape2)

#------------------------------------------------------------
# Gloval parameters
#------------------------------------------------------------
wlmax<-800
wlmin<-300
wlstd<-700
ayfact<-2.303
commln<-3

#------------------------------------------------------------
# Utilities
#============================================================
# Make figure
Make_figure<-function(tmp.df=blank.df,fdir=Ydir,fname="blank.pdf"){
	#tmp<-melt(tmp.df,id.vars="wL")
	#tmp<-melt(tmp.df,variable.name="wL")
	
	#print("Debug at 2019/07/03 --- Make_figure")
	#print(paste(head(tmp.df)),quote="FALSE")
	tmp<-melt(tmp.df,id="wL")
	pdf(paste(".",fdir,fname,sep="/"))
	g2<-ggplot(data=tmp,aes(x=wL,y=value,color=variable,group=variable))
	g2<-g2+geom_line(stat="identity")
	plot(g2)
	dev.off()
}

#============================================================
# Make full path
Make_path<-function( t2dir=tdir,t2fn=tfn ){
	return(paste(".",t2dir,t2fn,sep="/"))
}

#============================================================
# Make file for filelist
Make_fn<-function(Mdir=tdir,Mfn=tfn){
	print("Debug at 2019/4/27 --- Make_fn")
	#write.csv(file="filenamelist.csv", paste(dir(Mdir),collapse="¥n"), quote=FALSE,row.names=FALSE,col.names=NA)
	fnl<-dir(Mdir)
	fnl<-fnl[grep(".ASC",fnl)]
	print(paste("Mdir=",Mdir),quote=FALSE)
	print(paste("Mfn=",Mfn),quote=FALSE)
	
	print(Make_path(t2dir=Mdir,t2fn=Mfn),quote=FALSE)
	#for(i in 1:lenght(fnl)){fnl[i]<-strsplit(fnl[i])}
	write.csv(file=Make_path(t2dir=Mdir,t2fn=Mfn), fnl, quote=FALSE, row.names=FALSE ) 
	#CAUTION: in write.csv, col.naes option is ignored
}


#============================================================
# Read filelist
#flag:B= for blank
#flag:A= for data
Read_fl<-function(Rdir=tdir, Rfn=tfn, flag="B"){

	#print(paste("IN Read_fl Rdir :",Rdir," Rfn:",Rfn,sep=""))	
	Rfnd<-read.csv(Make_path(t2dir=Rdir,t2fn=Rfn),header=FALSE,skip=commln)
	
	if(flag=="B"){
		BRnf<-as.character(Rfnd[grep("^B",Rfnd[,1]),4])
		BRnf<-gsub(" ","",BRnf,fixed=TRUE) #delete space
		#BRnf<-gsub("[[:space:]]","",BRnf,fixed=TRUE) #delete space
		#BRnf<-gsub("t","",BRnf,fixed=TRUE) #delete space
		#print("debug in Read_fl delete tab and space for blank")
		#print(BRnf)		
		return(BRnf)
	} else if (flag=="A"){
		ARnf<-Rfnd[-grep("^B",Rfnd[,1]),]
		ARnf[,4]<-as.character(ARnf[,4])
		ARnf[,4]<-gsub(" ","",ARnf[,4],fixed=TRUE) #delete space
		#print("debug in Read_fl delete tab and space for data")
		#print(ARnf[,4])
		return(ARnf)		
	} else{
		return("1")
	}
	
}

#============================================================
# Function for calculation mean of blank
Calc_Blank<-function(bdir=tdir, bnf=BYnf, boutf="Yblank.csv"){
	
	
	tfn<-Make_path(t2dir=bdir,t2fn=bnf[1])
	#print(tfn)
	blank.df<-data.frame(read.csv(file=tfn,header=FALSE)) #hanger data.frame for blank 
	dimnames(blank.df)[[2]]<-c("wL",strsplit(bnf[1],".ASC")[[1]])
	bwlmax=ifelse(blank.df$wL[which.max(blank.df$wL)]<wlmax,which.max(blank.df$wL),which(blank.df$wL==wlmax))
	bwlmin=ifelse(blank.df$wL[which.min(blank.df$wL)]>wlmin,which.min(blank.df$wL),which(blank.df$wL==wlmin))
	#bwlmax=which(blank.df$wL==wlmax)
	#bwlmin=which(blank.df$wL==wlmin)
	#bwlmax=ifelse(length(bwlmax)==0,which.max(blank.df$wL),bwlmax)
	#bwlmin=ifelse(length(bwlmin)==0,which.min(blank.df$wL),bwlmin)
		
	if(0){ #for DEBUG
		print(paste("bwlmax=",bwlmax))
		print(paste("bwlmin=",bwlmin))
		print(paste("bwlmax length:",length(bwlmax)))
		print(paste("bwlmin length:",length(bwlmin)))
		print(paste("bwlmax max =",which.max(blank.df$wL)))
		print(paste("bwlmin minx =",which.min(blank.df$wL)))
		print(paste(blank.df[bwlmax,]),quote=FALSE)
		print(paste(blank.df[bwlmin,]),quote=FALSE)
	}
	
	
	if((bwlmax>0)&(bwlmin>0)){
		if(bwlmax>bwlmin){ blank.df<-blank.df[bwlmin:bwlmax,] }
		else{ blank.df<-blank.df[bwlmax:bwlmin,] }
	}
	
	for(i in 2:length(bnf)){
		print(paste("i=",i),quote=FALSE)
		tfn<-Make_path(t2dir=bdir,t2fn=bnf[i])
		tmp<-read.csv(tfn,header=FALSE) # read brank files
		#tmp<-tmp[which(tmp[,1]==wlmax):which(tmp[,1]==wlmin),]
		tmp<-tmp[bwlmax:bwlmin,]	
		blank.df<-cbind(blank.df,tmp[,2])
		dimnames(blank.df)[[2]][i+1]<-c(strsplit(bnf[i],".ASC")[[1]])
	}
	#print("Debug at 2019/7/3 --- Calc_Blank",quote=FALSE)
	#print(paste("bwlmax=",bwlmax,", bwlmin=",bwlmin))
	#calc average of blank
	blank.df$average<-as.numeric(apply(blank.df[,2:ncol(blank.df)],1,mean))
	write.csv(file=Make_path(t2dir=bdir,t2fn=boutf),blank.df,quote=FALSE)
	#print("Debug at 2019/7/3 --- Calc_Blank",quote=FALSE)
	
	return(blank.df)
	
}

#------------------------------------------------------------
# Calculations and drow
#============================================================
# AY
#============================================================
Calc_Ay<-function( Yfn=tfn, Ydir=tdir ){
	#1st-3rd lines must be skipped
	#1st clomn must be station name or blank
	#4th clomn must be filename
	
	#print("Debug at 2019/6/3 --- Calc_Ay",quote=FALSE)
	#print(paste("dir=",Ydir,", filename=",Yfn,sep=""),quote=FALSE)	
	
	#........................................................
	#  Calculation for Blank average
	#........................................................
	#define blank filename
	BYnf<-Read_fl(Rdir=Ydir, Rfn=Yfn, flag="B")
	print(paste0("BYnf:",BYnf))

	#read blank file
	Yblank.df<-Calc_Blank( bdir=Ydir, bnf=BYnf, boutf="Yblank.csv" )		
	#drow blank data
	Make_figure(tmp.df=Yblank.df,fdir=Ydir,fname="Yblank.pdf")	

	#........................................................
	#  Calculation for Ay
	#........................................................
	#define data filename
	DYnfd<-Read_fl(Rdir=Ydir, Rfn=Yfn, flag="A")
	
	#read wL
	tfn<-paste(".",Ydir,DYnfd[1,4],sep="/")
	#print(tfn)
	Ydata.df<-data.frame(read.csv(file=tfn,header=FALSE))[,1]
	
	#calc Ay for each sampling points
	tstp<-as.character(unique(DYnfd[,1]))
	for(i in 1:length(tstp)){
		tfn<-DYnfd[grep(tstp[i],DYnfd[,1]),4]
		tfn1<-Make_path(t2fn=tfn[1], t2dir=Ydir)
		tfn2<-Make_path(t2fn=tfn[2], t2dir=Ydir)
		
		tmp1<-read.csv(tfn1,header=FALSE)
		tmp2<-read.csv(tfn2,header=FALSE)
		
		t1wlmax=ifelse(max(tmp1[,1],na.rm=TRUE)<wlmax,which.max(tmp1[,1]),which(tmp1[,1]==wlmax))
		t1wlmin=ifelse(min(tmp1[,1],na.rm=TRUE)>wlmin,which.min(tmp1[,1]),which(tmp1[,1]==wlmin))
		t2wlmax=ifelse(max(tmp2[,1],na.rm=TRUE)<wlmax,which.max(tmp2[,1]),which(tmp2[,1]==wlmax))
		t2wlmin=ifelse(min(tmp2[,1],na.rm=TRUE)>wlmin,which.min(tmp2[,1]),which(tmp2[,1]==wlmin))
		
		tmp1<-tmp1[t1wlmax:t1wlmin,] #maximum range of wL:300~800
		tmp2<-tmp2[t2wlmax:t2wlmin,] #maximum range of wL:300~800

		tmpdf<-cbind(tmp1[,2],tmp2[,2])
		tmpdf<-cbind(tmpdf,sweep(tmpdf,1,Yblank.df$average,FUN="-"))
		tmp1700<-tmpdf[which(tmp1[,1]==wlstd),3]
		tmp2700<-tmpdf[which(tmp2[,1]==wlstd),4]
		tmp3<-cbind(ayfact*(tmpdf[,3]-tmp1700)/0.1,ayfact*(tmpdf[,4]-tmp2700)/0.1)
		tmpdf<-cbind(tmpdf,tmp3)
		tmpdf<-cbind(tmpdf,apply(tmpdf[,5:6],1,mean))	
		dimnames(tmpdf)[[2]]<-c(unlist(strsplit(tfn[1],".ASC")),
			unlist(strsplit(tfn[2],".ASC")),"samp1-bla","samp2-bla",
			"ay1","ay2",paste("ay_",tstp[i],sep=""))
		#print("Debug at 2019/4/30 -2-- Calc_Ay",quote=FALSE)
		Ydata.df<-cbind(Ydata.df,tmpdf)
	}
	tfn<-Make_path(t2fn="Yspectra.csv",t2dir=Ydir)
	dimnames(Ydata.df)[[2]][1]<-"wL"
	write.csv(file=tfn,Ydata.df,quote=FALSE)
	
	#drow Ay
	tdf<-as.data.frame(Ydata.df[,c(1,grep("^ay_",dimnames(Ydata.df)[[2]]))])
	#print(nrow(tdf))
	Make_figure(tmp.df=tdf,fdir=Ydir,fname="Ydata.pdf")	
	save(Ydata.df,file="Ydata.RData")
	
	return()
}

#============================================================
# AP or AD 
#============================================================
#same function
Calc_ApAD<-function( PDfn=tfn, PDdir=tdir ){
	print("Debug at 2019/6/03 --- Calc_ApAD")
	print(paste("dir=",PDdir,", filename=",PDfn,sep=""),quote=FALSE)	
	
	#........................................................
	#  Calculation for Blank average
	#........................................................
	#define blank filename
	BPnf<-Read_fl(Rdir=PDdir, Rfn=PDfn, flag="B")
	#read blank file
	PDblank.df<-Calc_Blank( bdir=PDdir, bnf=BPnf, boutf="Pblank.csv" )		
	#drow blank data
	Make_figure(tmp.df=PDblank.df,fdir=PDdir,fname="Pblank.pdf")	
	
	#........................................................
	#  Calculation for Ap
	#........................................................
	print("Debug at 2019/6/07 --- Calc_ApAD finish blank", quote=FALSE)

	#define data filename
	DPnfd<-Read_fl(Rdir=PDdir, Rfn=PDfn, flag="A")
	#print("dimnames DPnfd",quote=FALSE)
	#print(paste(dimnames(DPnfd)[[2]]), quote=FALSE)
	
	dimnames(DPnfd)[[2]]<-c("station","year","date","fname","fVol","cell1","cell2","cell3")
	#write.csv(DPnfd,file="./debug_settingfile.csv",quote=FALSE)

	#station name and number
	Stn<-unique(DPnfd$station)
	#print(paste("station",Stn))
	
	#Strage of AP
	ListAPAD<-list()

	#Calculation AP each station
	for(s in 1:length(Stn)){
	#for(s in 1:1){
		Sti<-DPnfd[DPnfd$station==Stn[s],] #Store station and file information
		#print(paste("station:",Stn[s]),quote=FALSE)
		#print(paste(Sti[1,],collapse=" "),quote=FALSE)
		
		#if year, station and date are not perfect matching　for each, the station is skipped.
		if(!(all(all(Sti$year==Sti$year[1]),all(Sti$date==Sti$date[1])))){
			print(paste("Station",Stn[s],"is skipped------------------"),quote=FALSE)
			next
		}
		#Store filtration volume
		tfVol<-Sti$fVol[!is.na(Sti$fVol)]
		#Filtration volume are not perfect matching, the station is skipped.
		if(length(tfVol)>1){
			if(!all(tfVol==tfVol[1])){
				print(paste("Station",Stn[s],"is skipped (tfVol aren't perfect matching)-----"),quote=FALSE)
				next
			}
			tfVol<-tfVol[1]
		}
		
		#Store list and average of cell size
		tSC1<-Sti$cell1[!is.na(Sti$cell1)] 
		if((length(tSC1)>1)||(length(tSC1)==0)){
			if(!all(tSC1==tSC1[1])){
				print(paste("Station",Stn[s],"is skipped (tSC1 aren't perfect matching)-----"),quote=FALSE)
				next
			}
			tSC1<-tSC1[1]
		}

		tSC2<-Sti$cell2[!is.na(Sti$cell2)] 
		if((length(tSC2)>1)||(length(tSC2)==0)){
			if(!all(tSC2==tSC2[1])){
				print(paste("Station",Stn[s],"is skipped (tSC2 aren't perfect matching)-----"),quote=FALSE)
				next
			}
			tSC2<-tSC2[1]
		}

		tSC3<-Sti$cell3[!is.na(Sti$cell3)] 
		if((length(tSC3)>1)||(length(tSC3)==0)){
			if(!all(tSC3==tSC3[1])){
				print(paste("Station",Stn[s],"is skipped (tSC3 aren't perfect matching)-----"),quote=FALSE)
				next
			}
			tSC3<-tSC3[1]
		}
		
		tSC<-c(tSC1,tSC2,tSC3,mean(c(tSC1,tSC2,tSC3)))
		if(0){
			print("debug at 2019/0703 ---------APAD---------1---")
			print(paste("tSC1=",tSC1),quote=FALSE)
			print(paste("tSC2=",tSC2),quote=FALSE)
			print(paste("tSC3=",tSC3),quote=FALSE)
			print(paste("mean=",mean(tSC1,tSC2,tSC3)),quote=FALSE)
			print(paste("mean=",mean(c(tSC1,tSC2,tSC3))),quote=FALSE)
			print(paste(tSC),quote=FALSE)
			print("debug at 2019/0703 ---------APAD---------1---")
		}
		tSC.a<-pi*tSC[4]*tSC[4]/4
		tSC.f<-2.303*tSC.a/tfVol
		
		
		#Set wL
		tfn<-paste(".",PDdir,Sti[1,4],sep="/") #filename: 4th clomn
		PDdata.df<-data.frame(read.csv(file=tfn,header=FALSE))[,1] #Strage of data
		
		#Read ap data
		for(i in 1:nrow(Sti)){		
			tfn<-paste(".",PDdir,Sti$fname[i],sep="/")
			tmp<-data.frame(read.csv(file=tfn,header=FALSE))[,2]
			PDdata.df<-cbind(PDdata.df,tmp)
		}
		dimnames(PDdata.df)[[2]]<-c("wL",Sti$fname)
		tcn1<-dimnames(PDdata.df)[[2]][grep(".ASC$",dimnames(PDdata.df)[[2]])]
		#tcn1<-Sti$fname
		if(0){
			#write.csv(file="debug_AP1.csv",PDdata.df,quote=FALSE)
			#write.csv(file="debug_AP_blank.csv",PDblank.df,quote=FALSE)
			print(paste(Sti$fname[i]))
			print(dimnames(PDdata.df)[[2]])
			print( paste(grep(".ASC$",dimnames(PDdata.df)[[2]]) ) )
			print(PDdata.df[1,grep(".ASC$",dimnames(PDdata.df)[[2]]) ])
			print(paste0("data",1,sep=""))
			print(PDdata.df[1,tcn1[1]])
			print(PDblank.df$average[1])
			print(PDdata.df[1,tcn1[1]]-PDblank.df$average[1])
			print(paste(tcn1))
			print(PDdata.df[,tcn1[1]])
			print(PDdata.df[,tcn1[2]])
			print("data 2 debug at 20190607--------------------------------")

			#in for
			print(paste0("clumn name is ",tcn2))
			print(paste0("clumn name is ",tcn1[j]))
			print(paste(dimnames(PDdata.df)[[2]]),quote=FALSE)
			print(paste(PDdata.df[,tcn1[j]]),quote=FALSE)
			print(paste0("length=",length(PDdata.df[,tcn1[j]])))
		}
		tmp.df<-data.frame(data1=rep(0,nrow(PDdata.df)))
		for(j in 1:(length(tcn1)-1) ){
			tmp.df<-cbind(tmp.df,rep(0,nrow(PDdata.df)))
			dimnames(tmp.df)[[2]][j+1]<-paste0("data",j+1)
		}
		for(j in 1:length(tcn1)){
			#print(paste0("j=",j))
			tcn2<-paste0("data",j,sep="")
			tmp.df[,tcn2]<-PDdata.df[,tcn1[j] ]-PDblank.df$average
		}
		PDdata.df<-cbind(PDdata.df,tmp.df)
		
		PDdata.df$average<-apply(PDdata.df[,grep("^data",dimnames(PDdata.df)[[2]])],1,mean,rm.na=TRUE)
		
		#standardization with value of maximum wave length.
		PDdata.df$ODf<-PDdata.df$average-PDdata.df$average[which.max(PDdata.df$wL)]
		PDdata.df$ODps<-0.378*PDdata.df$ODf+0.523*PDdata.df$ODf*PDdata.df$ODf
		PDdata.df$ap<-tSC.f*PDdata.df$ODps
		
		ListAPAD[[s]]<-list(station=Sti$station[1],year=Sti$year[1],
					date=Sti$date[1],fname=paste(Sti$fname,collapse=","),
					fVol=tfVol,SizeC=tSC,AreaC=tSC.a,FactorC=tSC.f,APADdata=PDdata.df)
		
	}
	
	#for debug
	tmp.df<-ListAPAD[[1]]$APADdata
	tmp2.df<-ListAPAD[[1]]$APADdata[,c("wL","ap")]
	tmpt<-paste0(ListAPAD[[1]]$year,ListAPAD[[1]]$date)
	dimnames(tmp2.df)[[2]]<-c("wL",paste(ListAPAD[[1]]$station,tmpt,sep="_") )
	#print( paste(dimnames(tmp2.df[[2]])) )
	#print(paste("Length of ListAPAD is ",length(ListAPAD)),quote=FALSE)
	if(length(ListAPAD)>1){
		for(i in 2:length(ListAPAD)){
			tmp.df<-cbind(tmp.df,ListAPAD[[i]]$APADdata)
			tmp2.df<-cbind(tmp2.df,ListAPAD[[i]]$APADdata$ap)
		}
		for(i in 2:length(ListAPAD)){
			tmpt<-paste0(ListAPAD[[i]]$year,ListAPAD[[i]]$date)
			dimnames(tmp2.df)[[2]][1+i]<-paste(ListAPAD[[i]]$station,tmpt,sep="_")
		}
	}
	write.csv(file=Make_path(t2dir=PDdir,t2fn="APAD.csv"),tmp.df,quote=FALSE)
	Make_figure(tmp.df=tmp2.df,fdir=PDdir,fname="APAD.pdf")
	save(ListAPAD,file=Make_path(t2dir=PDdir,t2fn="APAD.RData"))
	return(ListAPAD)
	
}

#============================================================
# Aph
#============================================================
Calc_Aph<-function( Pdir=tpdir, Pfn=tpfn, Ddir=tddir, Dfn=tdfn ){
	print("Debug at 2019/6/07 --- Calc_Aph")
	print(paste("AP:dir=",Pdir,", filename=",Pfn,sep=""),quote=FALSE)	
	print(paste("AD:dir=",Ddir,", filename=",Dfn,sep=""),quote=FALSE)
	#for windows
	#>C:\"Program Files"\R\R-3.5.3\bin\Rscript.exe AdApAy.R -ph test\ap\flist_p.csv  test\ad\flist_d.csv 
	#>C:\"Program Files"\R\R-3.5.3\bin\Rscript.exe AdApAy_ver01.R -ph ap/0301/flist_ap0301.csv  ad/StK/flist_adStK.csv 
	#for Mac
	#>Rscript AdApAy.R -ph test/ap/fnlist_p.csv  test/ad/flist_d.csv 

	#........................................................
	#  Calculation for AP
	#........................................................
	AP<-Calc_ApAD( PDfn=Pfn, PDdir=Pdir )
	print("Debug at 2019/6/07 --- Calc_Aph finish AP")
	
	#........................................................
	#  Calculation for AD
	#........................................................
	AD<-Calc_ApAD( PDfn=Dfn, PDdir=Ddir )
	#rename
	for(i in 1:length(AD)){ dimnames(AD[[i]]$APADdata)[[2]][9]<-"ad" }

	# Check same year, date and station (AP-AD)
	APH<-AP[[1]]$APADdata$wL
	for(i in 1:length(AP)){
		tmplap<-AP[[i]]
		
		for(j in 1:length(AD)){
			tmplad<-AD[[j]]
			flag<-(tmplap$station == tmplad$station)
			if(flag&(tmplap$year==tmplad$year)&(tmplap$date==tmplad$date)){
				APH<-cbind(APH,tmplap$APADdata$ap-tmplad$APADdata$ad)
			}
			
		}
	}

	dimnames(APH)[[2]]<-c("wL",as.character(sapply(AP,"[[","station")))
	print(paste("Debug at 2019/07/03 --2-- Calc_Aph----"))#for debug
	print(paste(dimnames(APH)[[2]]),quote="FALSE")

	write.csv(file=Make_path(t2dir="./",t2fn="APH.csv"),APH,quote=FALSE)
	Make_figure(tmp.df=as.data.frame(APH),fdir="./",fname="APH.pdf")
	save(APH,file="APH.RData")
	

}


#------------------------------------------------------------
#  Main 
#
targs = commandArgs(trailingOnly=TRUE)
#topt1<-"d"
#topt2<-""
topt1<-strsplit(targs[1],"-")[[1]][2]
topt2<-targs[2] #for windows command prompt
topt2<-gsub("\\","/",topt2,fixed=TRUE) #for windows command prompt
topt2<-strsplit(topt2,"/")[[1]]
topt3<-targs[3]
topt3<-gsub("\\","/",topt3,fixed=TRUE) #for windows command prompt
topt3<-strsplit(topt3,"/")[[1]]

print(paste("topt1=",topt1,sep=""),quote=FALSE)
print(paste("topt2=",topt2,sep=""),quote=FALSE)
print(paste("topt3=",topt3,sep=""),quote=FALSE)

#if( (match(topt1,"d")==1) ){

if( (topt1=="y") ){
	tfn<-topt2[length(topt2)]
	tdir<-paste(topt2[1:(length(topt2)-1)],collapse="/")
	#print("Debug at 2019/6/5 --- at topt1 == y",quote=FALSE)
	#print(paste("tfn = ",tfn,", tdir = ",tdir,sep=""),quote=FALSE)	
	Calc_Ay( Yfn=tfn, Ydir=tdir )
	q()
} else if( (topt1=="pd") ){
	tfn<-topt2[length(topt2)]
	tdir<-paste(topt2[1:(length(topt2)-1)],collapse="/")	
	Calc_ApAD( PDfn=tfn, PDdir=tdir )
	q()
} else if( (topt1=="ph") ){
#else if( (match(topt1,"py")==1) ){
	tpfn<-topt2[length(topt2)]
	tpdir<-paste(topt2[1:(length(topt2)-1)],collapse="/")	
	
	tdfn<-topt3[length(topt3)]
	tddir<-paste(topt3[1:(length(topt3)-1)],collapse="/")	
	Calc_Aph( Pdir=tpdir, Pfn=tpfn, Ddir=tddir, Dfn=tdfn )
	q()
} else if( (topt1=="f") ){
	#print("Debug at 2019/4/27  --- else if topt1")	
	#print(paste(topt2),quote=FALSE)
	#print(paste(topt2[length(topt2)]),quote=FALSE)
	tdir<-paste(topt2[1:(length(topt2)-1)],collapse="/")
	tfn<-topt2[length(topt2)]
	Make_fn( Mdir=tdir, Mfn=tfn )
	q()
} else{
	print("Usage: Rscript AdApAy.R [-y/p/pd/f] ./[target dir]/[file name]",quote=FALSE)
	print("-y :Calculation for Ay",quote=FALSE)
#	print("-pd :Calculation for Ap or Ad separately",quote=FALSE)
	print("-ph:Calculation for Aph",quote=FALSE)
	print("-f :Make a filename lists",quote=FALSE)
	q()
}
print("Debug at 2019/4/27")


