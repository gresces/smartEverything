package org.angrybirds.minictrl;

import androidx.appcompat.app.AppCompatActivity;

import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.SeekBar;
import android.widget.TextView;
import android.widget.Toast;

import org.w3c.dom.Text;

import java.net.*;
import java.io.*;
import java.nio.charset.StandardCharsets;


public class MainActivity extends AppCompatActivity {

    private Button btn;
    private Button btn_test;
    private TextView txt;
    private EditText etHost;
    private EditText etPort;
    private EditText etInfo;
    private SeekBar skb;

    String tag = this.toString();
    String text = "";
    String host = "120.48.100.193";
    Integer port = 3210;
    Integer light = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // TextView
        txt = (TextView)findViewById(R.id.txtOne);

        // EditView
        etHost = (EditText)findViewById(R.id.etHost);
        etPort = (EditText)findViewById(R.id.etPort);
        etInfo = (EditText)findViewById(R.id.etInfo);

        // Seekbar
        skb = (SeekBar)findViewById(R.id.skb_light);

        // button
        btn = (Button) findViewById(R.id.btn);
        btn_test = (Button)findViewById(R.id.btn_test);

        btn_test.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                etHost.setText(host.toString());
                etPort.setText(port.toString());
                etInfo.setText("Android".toString());
            }
        });

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                host = etHost.getText().toString();
                port = Integer.valueOf(etPort.getText().toString());
                light = skb.getProgress();
                text = host + port + etInfo.getText().toString() + "@" + light;
                new Thread(){
                    @Override
                    public void run(){
                        try {
                            UdpSend_switch();
                            txt.setText("OK" + text);
                        } catch (IOException e){
                            e.printStackTrace();
                            txt.setText("Fail");
                        }
                    }
                }.start();
            }
        });

        skb.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int i, boolean b) {
                btn.setText(i + "");
                btn.setTextSize(60);
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {

            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {
                host = etHost.getText().toString();
                port = Integer.valueOf(etPort.getText().toString());
                light = skb.getProgress();
                text = host + port + etInfo.getText().toString() + "@" + light;
                new Thread(){
                    @Override
                    public void run(){
                        try {
                            UdpSend_pulley();
                            txt.setText("OK" + text);
                        } catch (IOException e){
                            e.printStackTrace();
                            txt.setText("Fail");
                        }
                    }
                }.start();
            }
        });

    }

    void UdpSend_switch() throws IOException{
        InetAddress address = InetAddress.getByName(host);
        byte[] buf = (etInfo.getText().toString() +"@"+ light.toString() +"@"+ "0").getBytes(StandardCharsets.UTF_8);
//        byte[] buf = ("test" +"@"+ light.toString()).getBytes(StandardCharsets.UTF_8);
        DatagramPacket packet = new DatagramPacket(buf, buf.length, address, port);
//        DatagramPacket packet = new DatagramPacket(buf, buf.length, InetAddress.getByName("120.48.100.193"), 3210);
        DatagramSocket socket = new DatagramSocket();
        socket.send(packet);
        socket.close();
    }

    void UdpSend_pulley() throws IOException{
        InetAddress address = InetAddress.getByName(host);
        byte[] buf = (etInfo.getText().toString() +"@"+ light.toString() +"@"+ "1").getBytes(StandardCharsets.UTF_8);
//        byte[] buf = ("test" +"@"+ light.toString()).getBytes(StandardCharsets.UTF_8);
        DatagramPacket packet = new DatagramPacket(buf, buf.length, address, port);
//        DatagramPacket packet = new DatagramPacket(buf, buf.length, InetAddress.getByName("120.48.100.193"), 3210);
        DatagramSocket socket = new DatagramSocket();
        socket.send(packet);
        socket.close();
    }
}

