def crop_c(filenames):
    dir=filenames
    os.makedirs(os.path.join('.', 'white_edging_out'), exist_ok=True)
    tf=os.path.join('.', 'white_edging_out')
    print('output : ',tf)
    
    for file in dir:
 
        
        listf=file.split('/')
        #print(listf[-1])
        

        #imt1=cv2_ext.imread(r'{0}'.format(i))
        imt1=cv2.imread(file)
        

        if imt1 is None: 
            print('cannot imge read')   
   
        else :     
            try:
                imt=cv2.cvtColor(imt1,cv2.COLOR_BGR2GRAY)
                
                
                
                mu=0.08
                x,y=imt.shape
                x2=int(mu*x)
                y2=int(mu*y)
                x3=x-x2
                y3=y-y2

                imt2=imt[x2:x3,y2:y3]
                mean=int(np.mean(imt2.flatten()))
                mean_color=mean+8
                if (mean_color)>=255:
                    mean_color= mean
                
                imt=cv2.copyMakeBorder(imt,5,5,5,5,cv2.BORDER_CONSTANT,value=[mean_color,mean_color,mean_color])

                for i in range(x2,x3):
                    for j in range(y2,y3):

                        imt[i,j]=255

                ret, thresh = cv2.threshold(imt, 127, 255, 0)
                contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

                s=imt.size-(imt.size*0.02)
                p=(imt.size)*0.0004
                for c in range(len(list(contours))):
                        
                    cnt = contours[c]
                    A=cv2.contourArea(cnt)
                    if A>p  and A<s:
                        cv2.drawContours(imt1, cnt, -1,(mean_color,mean_color,mean_color),10)
                        cv2.fillPoly(imt1,  pts =[cnt],  color =(mean_color,mean_color,mean_color))
                        
                #cv2_ext.imwrite( r'{0}'.format(i),imt1)
                #os.chdir(os.path.join('.','white_edging_out'))
                cv2.imwrite(os.path.join(tf,listf[-1]),imt1)

                print('complit white_edg:',file)
            except :
                print('no file complit:',file)
    print('wahit_edg is complit')
#888888888888888888888888888888888888666666666666666666666666666666666        
def croper(filenames):
    dir=filenames

    # dir=glob2.glob(dir1+'/*.jpg', recursive=True)
    c=15
    for i in dir:
        
        im = Image.open(i)
 
        # Size of the image in pixels (size of original image)
        # (This is not mandatory)
        width, height = im.size
        
        # Setting the points for cropped image
        left = c
        top = c
        right = width-c
        bottom = height-c
        
        # Cropped image of above dimension
        # (It will not change original image)
        im1 = im.crop((left, top, right, bottom))
        
        # Shows the image in image viewer
        im1.save(i)
        print('crop ok:',i)
    print('crope is complit')