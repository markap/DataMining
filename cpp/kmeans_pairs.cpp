#include <utility>
#include <iostream>
#include <vector>
#include <random>
#include <map>
#include <cmath>

using std::cout;
using std::endl;
using std::vector;
using std::pair;
using std::make_pair;
using std::map;
using std::pow;
using std::sqrt;


void make_random_points(vector<pair<double, double> > *points, int number, int min=0, int max=100)
{


    // @see http://stackoverflow.com/a/7560564/468259
    std::random_device rd; // obtain a random number from hardware
    std::mt19937 eng(rd()); // seed the generator
    std::uniform_int_distribution<> distr(min, max); // define the range

    for(int n=0; n<number; ++n) 
    {
        points->push_back(make_pair(distr(eng), distr(eng)));    
    }
}


void make_test_points(vector<pair<double, double> > *points)
{
    points->push_back(make_pair(5,5)); 
    points->push_back(make_pair(10,5)); 
    points->push_back(make_pair(5,50)); 
    points->push_back(make_pair(60,50)); 
    points->push_back(make_pair(90,90)); 
    points->push_back(make_pair(80,50)); 
}

void make_random_centroids(pair<double, double> *centroids, int k, int min, int max)
{
    double centroidDistance = double(max)/(k+1);

    for(int n=0; n<k; ++n)
    {
        double centroid = min+ centroidDistance*(n+1);
        centroids[n] = make_pair(centroid, centroid);
    }
}




double euclideanDistance(pair<double, double> pair1, pair<double, double> pair2)
{
    double firstVal = pow(pair1.first - pair2.first, 2);
    double secondVal = pow(pair1.second - pair2.second, 2);

    return sqrt(firstVal + secondVal);
}


int main() 
{
    vector<pair<double, double> > points;
    int numberOfPoints = 10; 
    int minRange = 5;
    int maxRange = 100;
    int k = 2;

    pair<double, double> centroids[k];

    //make_test_points(&points);
    make_random_points(&points, numberOfPoints, minRange, maxRange);
    make_random_centroids(centroids, k, minRange, maxRange); 


    cout << "Init points are... " << endl;
    for (auto point: points)
    {
        cout << "(" << point.first << "," << point.second << ")" << endl;
    }

    cout << "Init centers are..." << endl;

    for (int i=0; i<k; ++i)
    {

        cout << "(" << centroids[i].first << "," << centroids[i].second << ")" << endl;
    }

    // assign each data point to a cluster
    map<pair<double, double>, int> labelsMap;

    // @todo pointer instead of reference???
    for (int i=0; i<numberOfPoints; ++i) 
    {
        labelsMap.insert(make_pair(points[i], 0));
    }





    
    while(true)
    {
        bool convergence = true; 

        cout << "assign points to cluster " << endl; 
        // find closest centroid for point
        for (int i=0; i<numberOfPoints; ++i)
        {
            // @todo fix this
            double min_distance = 10000.0;
            int cluster_label = 0;

            // check all centroids
            for (int j=0; j<k; ++j)
            {
                double distance = euclideanDistance(points[i], centroids[j]);  
                if (distance < min_distance) 
                {
                    min_distance = distance;
                    cluster_label = j;
                }
            }

            // check if new cluster found
            if (cluster_label != labelsMap.at(points[i]))
            {
                labelsMap.at(points[i]) = cluster_label;
                convergence = false;
            }

            cout << "point (" << points[i].first << ",";
            cout << points[i].second << ") assigned to cluster ";
            cout << cluster_label << endl;
            


        }

        
        if (convergence) 
        {
            break;
        }


        // calculate new cluster centroids
        vector<pair<double, double> > cum_points;
        vector<int> count_points;

        // default values for each centroid
        for (int i=0; i<k; ++i) 
        {
            count_points.push_back(0);
            cum_points.push_back(make_pair(0.0, 0.0));
        }

        // sum up the actual values
        for (auto label: labelsMap)
        {
            count_points[label.second]++;
            auto &point = cum_points[label.second];
            point.first += label.first.first;
            point.second += label.first.second;
        }

        cout << "new centroids..." << endl;

        for (int i=0; i<k; ++i)
        {
            cout << "[debug]" << cum_points[i].first << "," << cum_points[i].second << "debug" << endl;
            cout << "[debug] count " << count_points[i] << endl;

            centroids[i] = make_pair(cum_points[i].first/count_points[i],
                                        cum_points[i].second/count_points[i]);

            cout << "(" << centroids[i].first << "," << centroids[i].second << ")" << endl;
        }


               
    }

}




