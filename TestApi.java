package test;  
  
public class TestApi  
{  
    public String value = ""; 

    public TestApi(String value) { 
        this.value = value; 
    } 

    public String getData(String key){  
        return key;  
    }  
    public void printData(String key){  
        System.out.println(key);  
    }   
} 