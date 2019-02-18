#include "RapidJSONAdapter.h"


int main()
{
    std::string json = "{\"working\":\"false\"}";
	
	
    Document d;
    d.Parse(json);

    Value& w = d["working"];
    w.SetString("true", 4);

    StringBuffer buffer;
    Writer<StringBuffer> writer(buffer);
    d.Accept(writer);

    std::cout << buffer.GetString() << std::endl;
    return 0;
}
