import pickle
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import sklearn.metrics as sm


track_dict = pickle.load(
    open('../valence_space_data/data/track_dict.p', 'rb'))
tracks = pickle.load(
    open('../valence_space_data/data/cleanTracks.p', 'rb'))
dummied = pickle.load(
    open('../valence_space_data/data/dummied_df.p', 'rb'))

X_train, X_test, y_train, y_test = train_test_split(
    dummied.drop(['year', 'key', 'decade', 'time_signature'],
                 axis=1), dummied['decade'])

scaler = StandardScaler()
scaler.fit_transform(X_train)

rf = RandomForestClassifier(
    n_estimators=25, max_features=None, class_weight='auto')


if __name__ == '__main__':

    print 'cross val score: ',
    cross_val_score(rf, X_train, y_train, cv=5)

    rf.fit(X_train, y_train)

    predictions = rf.predict(scaler.transform(X_test))

    print sm.f1_score(predictions, y_test, average='macro')
    print sm.f1_score(y_test, predictions, average='weighted')
    print sm.f1_score(y_test, predictions, average='micro')
    print rf.score(X_test, y_test)
    print sm.mean_squared_error(predictions, y_test)
    print sm.mean_absolute_error(predictions, y_test)

    f = open('/models/forest_model.p', 'wb')
    pickle.dump(rf, f)
    f.close()

    f = open('/models/forest_model_scaler.p', 'wb')
    pickle.dump(scaler, f)
    f.close()
