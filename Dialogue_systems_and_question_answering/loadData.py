import json
import time
import random
import hashlib
import requests



def readData():
    TramRes = readTramData()
    ForeCastRes = readForecastData()
    restaurantRes = readRestaurant()
    return TramRes,ForeCastRes,restaurantRes


class tram():
    def __init__(self,tramName,stopLine):
        self.tramName = tramName
        self.stopLine = stopLine
    def __str__(self):
        return "tramName: %s ,stopLine: %s" \
               % (self.tramName, self.stopLine)


def readTramData():
    listRes = []
    dicts = {'content': [{'line_name': 'Guobo line (shaheba Lijia)', 'line_uid': 'c9c5acb091be753e06026fcd', 'pair_line_uid': 'c810960a8a3d3ac08adb73cd', 'stops': [{'is_practical': 1, 'name': 'Shaheba', 'uid': '54c6e6f1204e32fe455726c5', 'x': 11862664.99, 'y': 3462894.97}, {'is_practical': 0, 'name': 'Hongyanping', 'uid': '5913a215af909da1220262e4', 'x': 11861863.12, 'y': 3461472.2}, {'is_practical': 1, 'name': 'revival', 'uid': 'a26825f4bf51926300ff2d91', 'x': 11861947.8, 'y': 3460068.46}, {'is_practical': 0, 'name': 'think of source', 'uid': 'd34bce77f1e3a593f1193740', 'x': 11861856.11, 'y': 3458114.64}, {'is_practical': 0, 'name': "Liu's courtyard", 'uid': '01499cfc919e43f7e856fa0c', 'x': 11862435.52, 'y': 3454952.05}, {'is_practical': 0, 'name': 'Qingxi River', 'uid': 'a94a8d037e701d5e28201afe', 'x': 11861709.51, 'y': 3452632.72}, {'is_practical': 0, 'name': 'Wangjiazhuang', 'uid': 'cbdfd514c321db103be4a610', 'x': 11861430.79, 'y': 3450085.89}, {'is_practical': 0, 'name': 'Yuelai', 'uid': '70aeb6b9f3703f4b9f9d68cd', 'x': 11861696.45, 'y': 3447795.44}, {'is_practical': 0, 'name': 'China Expo Center', 'uid': '6ba7d477b905a6d4760269cd', 'x': 11861426.26, 'y': 3446627.94}, {'is_practical': 0, 'name': 'Gao Yikou', 'uid': '1aea71a384c97d800aa8d448', 'x': 11859484.33, 'y': 3444770.89}, {'is_practical': 0, 'name': 'Huangmaoping', 'uid': 'd92aba434e658ae1acee7a69', 'x': 11859871.77, 'y': 3441402.84}, {'is_practical': 0, 'name': 'Happy Valley', 'uid': '69b710e241556600badf8f55', 'x': 11857331.99, 'y': 3440459.44}, {'is_practical': 0, 'name': 'Lijia', 'uid': '0a699e02209a4f4bb15c6acd', 'x': 11855119.47, 'y': 3440290.44}]}, {'line_name': 'Guobo line (Lijia shaheba)', 'line_uid': 'c810960a8a3d3ac08adb73cd', 'pair_line_uid': 'c9c5acb091be753e06026fcd', 'stops': [{'is_practical': 0, 'name': 'Lijia', 'uid': '4e14ad3abc8eb39234b06ccd', 'x': 11855119.47, 'y': 3440290.44}, {'is_practical': 1, 'name': 'Happy Valley', 'uid': '9219802e25ffc9df2b3a9fe4', 'x': 11857331.99, 'y': 3440459.44}, {'is_practical': 1, 'name': 'Huangmaoping', 'uid': 'af4742fa82e1ff374afd3fae', 'x': 11859871.77, 'y': 3441402.84}, {'is_practical': 1, 'name': 'Gao Yikou', 'uid': 'a48b85002f9609e532870a5f', 'x': 11859484.33, 'y': 3444770.89}, {'is_practical': 1, 'name': 'China Expo Center', 'uid': '74249b8935dc0df92eb96dcd', 'x': 11861426.26, 'y': 3446627.94}, {'is_practical': 0, 'name': 'Yuelai', 'uid': '419712db8bb717f04c776ecd', 'x': 11861696.45, 'y': 3447795.44}, {'is_practical': 0, 'name': 'Wangjiazhuang', 'uid': '879005bcc816adb5acee7a1f', 'x': 11861430.79, 'y': 3450085.89}, {'is_practical': 1, 'name': 'Qingxi River', 'uid': '6ce4ece2baeafc8a4afd3fbe', 'x': 11861709.51, 'y': 3452632.72}, {'is_practical': 1, 'name': "Liu's courtyard", 'uid': 'f4503ed6182f081a0aa8d4aa', 'x': 11862435.52, 'y': 3454952.05}, {'is_practical': 1, 'name': 'think of source', 'uid': '864adc28469a7683b6f42fdc', 'x': 11861856.11, 'y': 3458114.64}, {'is_practical': 0, 'name': 'revival', 'uid': 'eb91d0c64a3a2137db13185c', 'x': 11861947.8, 'y': 3460068.46}, {'is_practical': 1, 'name': 'Hongyanping', 'uid': 'f03e32e6720a8ff233169b68', 'x': 11861863.12, 'y': 3461472.2}, {'is_practical': 0, 'name': 'Shaheba', 'uid': 'ea2930f84242ac546c4760b3', 'x': 11862664.99, 'y': 3462894.97}]}, {'line_name': "Rail transit line 4 (Min'an avenue to Tangjiatuo)", 'line_uid': '1ff3db9354ea19e9fda77895', 'pair_line_uid': '031258fd3fa58f6d6c3e1bd8', 'stops': [{'is_practical': 1, 'name': "Min'an Avenue", 'uid': '925bcc557fd95ec241afe69b', 'x': 11859635.29, 'y': 3432843.6}, {'is_practical': 1, 'name': 'North Square of Chongqing North Railway Station', 'uid': '6438d0434453f3a17ab55cf8', 'x': 11861976.06, 'y': 3433353.68}, {'is_practical': 0, 'name': 'Toutang', 'uid': 'e12c34e11f3fca254107c174', 'x': 11864528.74, 'y': 3432732.73}, {'is_practical': 0, 'name': 'Bonded port', 'uid': '259de0119b597b2a8c55ec1b', 'x': 11865686.36, 'y': 3433827.49}, {'is_practical': 0, 'name': 'Cuntan', 'uid': '0b4bbb4610bd76c1b33c8184', 'x': 11868206.35, 'y': 3434451.11}, {'is_practical': 0, 'name': 'Black stone', 'uid': '0f404bbba6902384a5da3962', 'x': 11869882.94, 'y': 3434798.65}, {'is_practical': 1, 'name': 'Taipingchong', 'uid': '2975d0719bc8431e46e274d5', 'x': 11872170.73, 'y': 3432386.17}, {'is_practical': 0, 'name': 'Tangjiatuo', 'uid': 'b4c116c3534db5430bccdddb', 'x': 11874128.02, 'y': 3432401.57}]}, {'line_name': 'Rail transit line 5 (Yuanbo center dashiba)', 'line_uid': '7f724f0c2cad0dd65bf6be69', 'pair_line_uid': '831a7fa7f3d60c1b7c29bde2', 'stops': [{'is_practical': 1, 'name': 'Park Expo Center', 'uid': '3580ac7998e1efd5dfee8bba', 'x': 11863128.31, 'y': 3441356.7}, {'is_practical': 0, 'name': 'Red crane', 'uid': '3d543c04099572ec60180979', 'x': 11862044.95, 'y': 3440257.1}, {'is_practical': 1, 'name': 'Huxia Street', 'uid': 'eb08995abe96d2663a13fd99', 'x': 11860672.96, 'y': 3439328.91}, {'is_practical': 0, 'name': 'see the light again', 'uid': 'c63f44253fa25bc1badf8f1b', 'x': 11859708.15, 'y': 3437927.66}, {'is_practical': 0, 'name': 'Harmony Road', 'uid': 'a9babef2c9eea4e2085cb388', 'x': 11860100, 'y': 3435503.2}, {'is_practical': 0, 'name': 'People and', 'uid': 'bf7de37c89a9d2b5581093a5', 'x': 11858867.96, 'y': 3434650.52}, {'is_practical': 0, 'name': 'Happy square', 'uid': 'd18d357e3c686dd6fd0eb031', 'x': 11857300.93, 'y': 3433829.74}, {'is_practical': 0, 'name': 'Ranjiaba', 'uid': '08692e30b8c2b82043ab9abc', 'x': 11856273.24, 'y': 3431480.75}, {'is_practical': 1, 'name': 'DALONGSHAN', 'uid': '80a83302938744ff16a1905f', 'x': 11856242.66, 'y': 3430383.5}, {'is_practical': 1, 'name': 'Dashiba', 'uid': 'cfdbeee4f727f950ca1b95bf', 'x': 11855848.04, 'y': 3427936.88}]}, {'line_name': 'Rail transit line 5 (dashiba Yuanbo Center)', 'line_uid': '831a7fa7f3d60c1b7c29bde2', 'pair_line_uid': '7f724f0c2cad0dd65bf6be69', 'stops': [{'is_practical': 0, 'name': 'Dashiba', 'uid': '01ad7b8f5245e0bdc9c3db10', 'x': 11855848.04, 'y': 3427936.88}, {'is_practical': 0, 'name': 'DALONGSHAN', 'uid': '3d44f3e543cc7c4e306212f4', 'x': 11856242.66, 'y': 3430383.5}, {'is_practical': 1, 'name': 'Ranjiaba', 'uid': 'dc5c192afcd3e1fa3b04b1a0', 'x': 11856273.24, 'y': 3431480.75}, {'is_practical': 1, 'name': 'Happy square', 'uid': '105e1a9ab8b355d12fb96de2', 'x': 11857300.93, 'y': 3433829.74}, {'is_practical': 1, 'name': 'People and', 'uid': 'f6fe2ddb4ff96ae524d2bb25', 'x': 11858867.96, 'y': 3434650.52}, {'is_practical': 1, 'name': 'Harmony Road', 'uid': '008527e4da5f2ec913293577', 'x': 11860100, 'y': 3435503.2}, {'is_practical': 1, 'name': 'see the light again', 'uid': '42d52995bf56a929276e98f5', 'x': 11859708.15, 'y': 3437927.66}, {'is_practical': 0, 'name': 'Huxia Street', 'uid': '9e5bc5882dda12e032f71d62', 'x': 11860672.96, 'y': 3439328.91}, {'is_practical': 1, 'name': 'Red crane', 'uid': 'd5a89723aad5e0b8c9c3db5a', 'x': 11862044.95, 'y': 3440257.1}, {'is_practical': 0, 'name': 'Park Expo Center', 'uid': '9510d3a903f7a2d0d62ce284', 'x': 11863128.31, 'y': 3441356.7}]}, {'line_name': 'South section of rail transit line 5 (Shiqiaopu Tiaodeng)', 'line_uid': 'd20e4e3836b646cf6f47608e', 'pair_line_uid': 'be42bd0a83d6756438221ce1', 'stops': [{'is_practical': 1, 'name': 'Stone bridge shop', 'uid': 'c861965407cad5ba05fef57b', 'x': 11854707.29, 'y': 3423104.46}, {'is_practical': 1, 'name': 'Shixin Road', 'uid': 'ae94b03880dfdafd3f9a5e30', 'x': 11853934.6, 'y': 3422271.89}, {'is_practical': 1, 'name': 'Bashan', 'uid': '1663099bbd665ac4deee8bea', 'x': 11852930.79, 'y': 3421596.3}, {'is_practical': 0, 'name': 'Fengxi Road', 'uid': '797a5fc809e992742fb96dda', 'x': 11851255.15, 'y': 3420739.59}, {'is_practical': 0, 'name': 'Chongqing West Railway Station', 'uid': 'd5361c7b2991816f10293549', 'x': 11849619.63, 'y': 3419034.65}, {'is_practical': 0, 'name': 'Huayan Temple', 'uid': 'a5e50d22e44859b2a0a93480', 'x': 11850314.58, 'y': 3418236.67}, {'is_practical': 0, 'name': 'Huacheng Road', 'uid': '10265b3dbb05122bdbeced99', 'x': 11851190.07, 'y': 3416498.41}, {'is_practical': 0, 'name': 'Mid level', 'uid': 'debbb632166138ffa8f7299c', 'x': 11850862.85, 'y': 3415605.91}, {'is_practical': 1, 'name': 'Zhongliang mountain', 'uid': '8955e0e06768d347dbd89161', 'x': 11850366.44, 'y': 3413840.64}, {'is_practical': 0, 'name': 'Jin Jianlu', 'uid': 'fc9bdf8077e631dae215f947', 'x': 11849928.29, 'y': 3411719.44}, {'is_practical': 0, 'name': 'Huayan Center', 'uid': '66703f49ce6f111fdb131879', 'x': 11849741.22, 'y': 3410001.34}, {'is_practical': 1, 'name': 'Tiaodeng', 'uid': 'f1d8da7f28e7d8149122e0c6', 'x': 11849435.04, 'y': 3407358.02}]}, {'line_name': 'South section of rail transit line 5 (Tiaodeng Shiqiaopu)', 'line_uid': 'be42bd0a83d6756438221ce1', 'pair_line_uid': 'd20e4e3836b646cf6f47608e', 'stops': [{'is_practical': 0, 'name': 'Tiaodeng', 'uid': '79327151bd16f96ce31103fc', 'x': 11849435.04, 'y': 3407358.02}, {'is_practical': 1, 'name': 'Huayan Center', 'uid': '172192addb3809cd7369d3fe', 'x': 11849741.22, 'y': 3410001.34}, {'is_practical': 1, 'name': 'Jin Jianlu', 'uid': '6ce014e2714a181fc51e51f8', 'x': 11849928.29, 'y': 3411719.44}, {'is_practical': 0, 'name': 'Zhongliang mountain', 'uid': '6cf70265219552ceaeb22a7f', 'x': 11850366.44, 'y': 3413840.64}, {'is_practical': 1, 'name': 'Mid level', 'uid': '630b5ad91677c1c546572681', 'x': 11850862.85, 'y': 3415605.91}, {'is_practical': 1, 'name': 'Huacheng Road', 'uid': 'be5b6d0776e627214e5547f2', 'x': 11851190.07, 'y': 3416498.41}, {'is_practical': 1, 'name': 'Huayan Temple', 'uid': 'df8dde4686a26bc5130daa84', 'x': 11850314.58, 'y': 3418236.67}, {'is_practical': 0, 'name': 'Chongqing West Railway Station', 'uid': '9dc3b4e79c42264345e27467', 'x': 11849619.63, 'y': 3419034.65}, {'is_practical': 1, 'name': 'Fengxi Road', 'uid': 'ff6ef0edc978c08d4c3a59dc', 'x': 11851255.15, 'y': 3420739.59}, {'is_practical': 0, 'name': 'Bashan', 'uid': 'd43cb3f0b7d28cf142d63e0a', 'x': 11852930.79, 'y': 3421596.3}, {'is_practical': 0, 'name': 'Shixin Road', 'uid': '497045792bd5f49e01897211', 'x': 11853934.6, 'y': 3422271.89}, {'is_practical': 0, 'name': 'Stone bridge shop', 'uid': 'c7ad11bead7886c7871541b7', 'x': 11854707.29, 'y': 3423104.46}]}], 'result': {'ccode': '132', 'qt': 'bsi'}}

    for i in dicts['content']:
        stops = []
        for stop in i['stops']:
            stops.append(stop['name'])
        listRes.append(tram(tramName=i['line_name'],stopLine=stops))

    return listRes

#Restaurant objects
class Restaurant():
    def __init__(self,region,categoryName,score,shopName,brandName,avgPrice):
        self.region =region
        self.categoryName = categoryName
        self.score = score
        self.shopName = shopName
        self.brandName = brandName
        self.avgPrice = avgPrice

    def __str__(self):
        return "region: %s ,categoryName: %s ,score:%s,shopName:%s,brandName:%s" \
               % (self.region, self.categoryName,self.score,self.shopName,self.brandName)

#Read restaurant data
def readRestaurant():
    reslut = []
    with open('../data/restaurant.json', encoding='utf-8') as file:
        data = file.read()
        res = json.loads(str(data))
        for item in res['shopBeans']:
            reslut.append(Restaurant(region=item['mainRegionName'],
                                  categoryName=item['mainCategoryName'],score=item['refinedScore2'],
                                  shopName=item['shopName'],brandName=item['branchName'],avgPrice=item['avgPrice']))
    return reslut

#Read weather data
def readForecastData():
    res = []
    #Define read path
    with open('../data/forecastData',encoding='utf-8') as file:
        #Read by line
        lineList = file.readlines()
        for item in lineList:
            dataAndForcast = item.split(":")

            res.append(foreCast(data=dataAndForcast[0],forecast= dataAndForcast[1].split("\n")[0]))
        return res
#Weather data entity
class foreCast():
    def __init__(self,data,forecast):
        self.data = data
        self.forecast = forecast
    def __str__(self):
        return "data: %s forcast: %s"%(self.data,self.forecast)


if __name__ == '__main__':
    for item in readTramData():
        print(item)