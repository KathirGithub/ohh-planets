import cv2 

solar=cv2.imread('solar-system.jpg')
cv2.putText(solar,'Sun',(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(solar,'Mercury',(115,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(solar,'Venus',(215,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(solar,'Earth',(315,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(solar,'Mars',(415,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(solar,'Jupiter',(515,350),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(solar,'Saturn',(815,350),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(solar,'Uranus',(1015,350),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(solar,'Neptune',(1115,350),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.imshow('open',solar)
cv2.waitKey(0)