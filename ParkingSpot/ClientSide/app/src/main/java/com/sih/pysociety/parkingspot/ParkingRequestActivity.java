package com.sih.pysociety.parkingspot;

import android.app.Dialog;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class ParkingRequestActivity extends AppCompatActivity {

    Button requestParking,logout;
    Dialog dlg;
    EditText oldpass,newpass;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_parking_request);
        requestParking = (Button)findViewById(R.id.btn_reqPark);
        requestParking.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent resultsActivity = new Intent(ParkingRequestActivity.this,ResultsActivity.class);
                startActivity(resultsActivity);
                finish();
            }
        });
        logout = (Button)findViewById(R.id.btn_logout);
        logout.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent loginActivity = new Intent(ParkingRequestActivity.this,LoginActivity.class);
                startActivity(loginActivity);
                finish();
            }
        });
    }
}


