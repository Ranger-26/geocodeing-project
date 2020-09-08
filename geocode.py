from geopy.geocoders import ArcGIS#import the module that gets the geolocation
import pandas as pd#imports the module to organize our data

def geocode(address):#This function takes in an address and returns lat and lo
    nom = ArcGIS()
    try:
        x=nom.geocode(address)
        return (x.latitude,x.longitude)
    except AttributeError:
        return('Nan',"Nan")


class File():
    def __init__(self,file):
        try:
            x=pd.read_csv(file)
            self.df=pd.DataFrame(x)
        except:
            self.df=None
    def get_addresses(self):
        try:
            return self.df.Address
        except:
            try:
                return self.df.address
            except:
                return None
    def modify_file(self):
        add=self.get_addresses()
        latitutes=[]
        longitudes=[]
        try:
            for a in add:
                y=geocode(a)
                latitude=y[0]
                longitude=y[1]
                latitutes.append(latitude)
                longitudes.append(longitude)

            self.df["Latitude"]=latitutes
            self.df['Longitude']=longitudes

            return self.df

        except:
            return 'Please make sure you have a column in your csv file called address or Address'
