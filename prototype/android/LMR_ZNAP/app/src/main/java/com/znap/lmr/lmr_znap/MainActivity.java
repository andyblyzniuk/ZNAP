package com.znap.lmr.lmr_znap;

/**
 * Created by Andy Blyzniuk on 01.11.2017.
 */
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;


public class MainActivity extends AppCompatActivity {
    private int user_id;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,WindowManager.LayoutParams.FLAG_FULLSCREEN);
        setContentView(R.layout.activity_main);
        Bundle bundle = getIntent().getExtras();
        assert bundle != null;
        user_id = bundle.getInt("userid");
            System.out.println("Main activity:" + user_id);

        findViewById(R.id.bLeaveReview).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent openRateActivity = new Intent(MainActivity.this, RateActivity.class);

                openRateActivity.putExtra("userid",user_id);
                startActivity(openRateActivity);
            }
        });

        findViewById(R.id.bRecordToZnap).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent openRecordToZnapActivity = new Intent(MainActivity.this, RecordToZnapActivity.class);

                startActivity(openRecordToZnapActivity);
            }
        });

        findViewById(R.id.bQueueState).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent openQueueStateActivity = new Intent(MainActivity.this, QueueStateActivity.class);

                startActivity(openQueueStateActivity);
            }
        });

        findViewById(R.id.bOwnCabinet).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent openQueueStateActivity = new Intent(MainActivity.this, OwnCabinetActivity.class);

                startActivity(openQueueStateActivity);

                Intent mainIntent = new Intent(MainActivity.this, OwnCabinetActivity.class);
                mainIntent.putExtra("userid", user_id);
                startActivity(mainIntent);


            }
        });

        findViewById(R.id.bOnline).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent callOnline = new Intent(Intent.ACTION_DIAL);
                callOnline.setData(Uri.parse("tel:0971735178"));
                startActivity(callOnline);
            }
        });

        findViewById(R.id.ibtFacebook).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent openFacebook= new Intent(Intent.ACTION_VIEW);
                openFacebook.setClassName("com.facebook.цнап", "com.facebook.цнап.MainActivity");
                Long uid = new Long("123456789");
                openFacebook.putExtra("extra_user_id", uid);
                startActivity(openFacebook);

            }
        });

    }

}

