{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "35f9360c-1e5b-4bf7-943b-9605efe9cd1d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   user_id             name  gender  age                     address  \\\n",
      "0        1     Anthony Wolf    male   73    New Rachelburgh-VA-49583   \n",
      "1        2  James Armstrong    male   56  North Jillianfort-UT-86454   \n",
      "2        3        Cody Shaw    male   75         North Anne-SC-53799   \n",
      "3        4  Sierra Hamilton  female   76     New Angelafurt-ME-46190   \n",
      "4        5      Chase Davis    male   31    South Bethmouth-WI-18562   \n",
      "\n",
      "  date_joined  \n",
      "0  2019/03/13  \n",
      "1  2020/11/06  \n",
      "2  2004/05/29  \n",
      "3  2005/08/26  \n",
      "4  2018/04/30  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv('users_v.csv')\n",
    "\n",
    "print(df.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3fbfe876-4830-4a8e-bb75-bea041152418",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   user_id             name  gender  age                     address  \\\n",
      "0        1     Anthony Wolf    male   73    New Rachelburgh-VA-49583   \n",
      "1        2  James Armstrong    male   56  North Jillianfort-UT-86454   \n",
      "2        3        Cody Shaw    male   75         North Anne-SC-53799   \n",
      "3        4  Sierra Hamilton  female   76     New Angelafurt-ME-46190   \n",
      "4        5      Chase Davis    male   31    South Bethmouth-WI-18562   \n",
      "5        6   Sierra Andrews  female   21          Ryanville-MI-69690   \n",
      "6        7        Ann Stone  female   41         Smithmouth-SD-17340   \n",
      "7        8     Karen Santos  female   34         Mariaville-AK-29888   \n",
      "8        9     Ronald Meyer    male   41  North Cherylhaven-NJ-04197   \n",
      "9       10    Steven Rivera    male   43          Wayneside-VT-29040   \n",
      "\n",
      "  date_joined  \n",
      "0  2019/03/13  \n",
      "1  2020/11/06  \n",
      "2  2004/05/29  \n",
      "3  2005/08/26  \n",
      "4  2018/04/30  \n",
      "5  2007/05/25  \n",
      "6  2005/01/05  \n",
      "7  2003/12/12  \n",
      "8  2015/11/14  \n",
      "9  2003/05/15  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df = pd.read_csv('users_v.csv')\n",
    "print(df.head(10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f3167351-f4ad-458e-b59e-836eac7b6209",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Youngest Age: 18 Oldest Age: 80\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv('users_v.csv')\n",
    "\n",
    "print(\"Youngest Age:\", df['age'].min(), \"Oldest Age:\", df['age'].max())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "81aec706-578b-4ae6-b567-2215a7c359b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "count    2357.000000\n",
      "mean       49.054731\n",
      "std        18.206348\n",
      "Name: age, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv('users_v.csv')\n",
    "\n",
    "print(df['age'].describe()[['count', 'mean', 'std']])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "b6d665b8-e9cb-477e-a3a4-579b541ec9be",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              name    surname\n",
      "0     Anthony Wolf       Wolf\n",
      "1  James Armstrong  Armstrong\n",
      "2        Cody Shaw       Shaw\n",
      "3  Sierra Hamilton   Hamilton\n",
      "4      Chase Davis      Davis\n"
     ]
    }
   ],
   "source": [
    "print(df.assign(surname=df['name'].apply(lambda x: x.split()[-1]))[['name', 'surname']].head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "33f8af89-6f49-405a-b830-7d69d0fc60ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      user_id                 name  gender  age                    address  \\\n",
      "2347     2348     Victoria Edwards  female   68    Lake Jamesberg-NY-88824   \n",
      "2348     2349          Chris Ellis    male   46  Port Richardside-NY-77994   \n",
      "2349     2350       Kimberly Smith  female   19      East Anthony-GA-00646   \n",
      "2350     2351       William Nelson    male   67   Lake Parkerside-MN-06905   \n",
      "2351     2352          Nancy Clark  female   80        Jamesshire-AK-88437   \n",
      "2352     2353      Brittney Graham  female   40         Brownland-CO-71229   \n",
      "2353     2354      Allison Schmidt  female   43        Port Logan-MD-38588   \n",
      "2354     2355  Christopher Johnson    male   68   North Justinton-VA-32798   \n",
      "2355     2356           Mark Brown    male   67    New Kayleefurt-MA-82581   \n",
      "2356     2357      Steven Robinson    male   45         Mistytown-HI-31737   \n",
      "\n",
      "     date_joined   surname  \n",
      "2347  2001/09/03   Edwards  \n",
      "2348  2011/03/18     Ellis  \n",
      "2349  2021/06/20     Smith  \n",
      "2350  2005/12/21    Nelson  \n",
      "2351  2001/12/12     Clark  \n",
      "2352  2005/07/10    Graham  \n",
      "2353  2008/11/30   Schmidt  \n",
      "2354  2006/08/01   Johnson  \n",
      "2355  2013/11/16     Brown  \n",
      "2356  2015/03/21  Robinson  \n"
     ]
    }
   ],
   "source": [
    "print(df.tail(10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "bdc9f461-2b5c-46ea-96a0-ca13e4d117d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['date_joined'] = pd.to_datetime(df['date_joined'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "d988d01c-eec5-4fff-b00a-31ce7b826f8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      user_id                 name  gender  age                    address  \\\n",
      "2347     2348     Victoria Edwards  female   68    Lake Jamesberg-NY-88824   \n",
      "2348     2349          Chris Ellis    male   46  Port Richardside-NY-77994   \n",
      "2349     2350       Kimberly Smith  female   19      East Anthony-GA-00646   \n",
      "2350     2351       William Nelson    male   67   Lake Parkerside-MN-06905   \n",
      "2351     2352          Nancy Clark  female   80        Jamesshire-AK-88437   \n",
      "2352     2353      Brittney Graham  female   40         Brownland-CO-71229   \n",
      "2353     2354      Allison Schmidt  female   43        Port Logan-MD-38588   \n",
      "2354     2355  Christopher Johnson    male   68   North Justinton-VA-32798   \n",
      "2355     2356           Mark Brown    male   67    New Kayleefurt-MA-82581   \n",
      "2356     2357      Steven Robinson    male   45         Mistytown-HI-31737   \n",
      "\n",
      "     date_joined   surname  \n",
      "2347  2001-09-03   Edwards  \n",
      "2348  2011-03-18     Ellis  \n",
      "2349  2021-06-20     Smith  \n",
      "2350  2005-12-21    Nelson  \n",
      "2351  2001-12-12     Clark  \n",
      "2352  2005-07-10    Graham  \n",
      "2353  2008-11-30   Schmidt  \n",
      "2354  2006-08-01   Johnson  \n",
      "2355  2013-11-16     Brown  \n",
      "2356  2015-03-21  Robinson  \n"
     ]
    }
   ],
   "source": [
    "print(df.tail(10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "356bbbbb-093b-4cd9-aa11-079db390f5b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['date_joined'] = pd.to_datetime(df['date_joined'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "940661d4-9a46-4795-bed9-6952eb1120ed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      user_id                 name  gender  age                    address  \\\n",
      "2347     2348     Victoria Edwards  female   68    Lake Jamesberg-NY-88824   \n",
      "2348     2349          Chris Ellis    male   46  Port Richardside-NY-77994   \n",
      "2349     2350       Kimberly Smith  female   19      East Anthony-GA-00646   \n",
      "2350     2351       William Nelson    male   67   Lake Parkerside-MN-06905   \n",
      "2351     2352          Nancy Clark  female   80        Jamesshire-AK-88437   \n",
      "2352     2353      Brittney Graham  female   40         Brownland-CO-71229   \n",
      "2353     2354      Allison Schmidt  female   43        Port Logan-MD-38588   \n",
      "2354     2355  Christopher Johnson    male   68   North Justinton-VA-32798   \n",
      "2355     2356           Mark Brown    male   67    New Kayleefurt-MA-82581   \n",
      "2356     2357      Steven Robinson    male   45         Mistytown-HI-31737   \n",
      "\n",
      "     date_joined   surname  \n",
      "2347  2001-09-03   Edwards  \n",
      "2348  2011-03-18     Ellis  \n",
      "2349  2021-06-20     Smith  \n",
      "2350  2005-12-21    Nelson  \n",
      "2351  2001-12-12     Clark  \n",
      "2352  2005-07-10    Graham  \n",
      "2353  2008-11-30   Schmidt  \n",
      "2354  2006-08-01   Johnson  \n",
      "2355  2013-11-16     Brown  \n",
      "2356  2015-03-21  Robinson  \n"
     ]
    }
   ],
   "source": [
    "print(df.tail(10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3bdaefd8-ae26-4296-a762-99ea99833619",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
