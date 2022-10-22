#include "settings.h"

using namespace cv;
using namespace std;

int main(int argc, char** argv) {

    Mat image = cv::imread( filePath + "/Captura.png");
    if(image.empty()) {
        cerr << "Error reading image" << endl;
        return 1;
    }
    else{
        cout<<"funciona";
        imshow("imagen" , image);
        Mat greyMat;
        cvtColor(image, greyMat, COLOR_BGR2GRAY);
        imshow("Imagen en escala de gris", greyMat);
        waitKey(0); 
        destroyAllWindows();    
    }
    
}
