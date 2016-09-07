package myutils;

import java.net.URLEncoder;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

import org.apache.commons.codec.binary.Base64;

public class Tools {
	public static String getHmacSHA1(String message, String key) {
        String hmacSha1 = null;
        try {
               // url encode
               message = URLEncoder.encode(message, "UTF-8");
               System.out.println(message);
               // hmac-sha1
               Mac mac = Mac.getInstance("HmacSHA1");
               SecretKeySpec spec = new SecretKeySpec(key.getBytes(), "HmacSHA1");
               mac.init(spec);
               byte[] byteHMAC = mac.doFinal(message.getBytes());
               // base64 encode
               System.out.println(new String(byteHMAC,"UTF-8"));
               hmacSha1 = new String(Base64.encodeBase64(byteHMAC));
        } catch (Exception e) {
               System.out.println("error");
        }
        return hmacSha1;
   }
}
