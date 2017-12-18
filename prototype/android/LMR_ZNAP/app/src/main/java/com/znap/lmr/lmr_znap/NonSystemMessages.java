package com.znap.lmr.lmr_znap;

import android.content.Context;
import android.content.DialogInterface;
import android.support.v7.app.AlertDialog;

/**
 * Created by Zava on 12.12.2017.
 */

public class NonSystemMessages {
    public static final String FIELD_MUST_BE_NOT_EMPTY = "Поле має бути заповнене";
    public static final String ENABLE_INTERNET_REQUEST = "Увімкніть, будь ласка, інтернет";
    public static final String OKAY = "Oк";
    public static final String FIELD_IS_NOT_ENTERED_CORRECTLY = "Some data is not entered correctly";
    public static final String NOT_VALID = "Not Valid";
    public static final String VALID = "Valid";

    public AlertDialog.Builder buildDialog(Context c) {
        AlertDialog.Builder builder = new AlertDialog.Builder(c);
        builder.setTitle(SystemMessages.NO_INERNET_CONNECTION);
        builder.setMessage(NonSystemMessages.ENABLE_INTERNET_REQUEST);
        builder.setPositiveButton(NonSystemMessages.OKAY, new DialogInterface.OnClickListener() {

            @Override
            public void onClick(DialogInterface dialog, int which) {
            }
        });
        return builder;
    }
}