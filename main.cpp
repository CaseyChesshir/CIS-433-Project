#include <iostream>
#include <thread>
#include <vector>
#include <unistd.h>
#include <stdlib.h>
#include <ctime>
#include <string>


void scrape(std::string filename){
	char *file = const_cast<char*> (filename.c_str());
	char *args[] = {"python3", "topsitescraper.py", file, NULL};	

	pid_t scraperpid = fork();

	if (scraperpid < 0){
		std::cout << "forking failed" << std::endl;
		exit(1);
	}	

	else if (scraperpid == 0){
		std::cout << "I am the scraper process, about to launch" << std::endl;
		execvp(args[0],args);
	}

}

int main(){

	//Website websites[500];

	// begin topsitescraper.py
	time_t t = time(0);
	struct tm * now = localtime( &t );
	std::string foldertime = "mkdir data/" + std::to_string(now->tm_year + 1900) + "-" + std::to_string(now->tm_mon) + "-" + std::to_string(now->tm_mday) + "-" + std::to_string(now->tm_hour) + "h" + std::to_string(now->tm_min) + "m" + std::to_string(now->tm_sec) + "s"; 
	system(foldertime.c_str());
	foldertime = foldertime.substr(5,std::string::npos);
	std::cout << "sending scraper off" << std::endl;	
	system(("python3 topsitescraper.py " + foldertime + "/top500sites.txt").c_str());
	std::cout << "scraper joined back" << std::endl;

	std::cout << "sending ips.sh off" << std::endl;
	system(("./ips.sh " + foldertime + "/top500sites.txt " + foldertime + "/top500IPs.txt").c_str());
	std::cout << "ips.sh joined back" << std::endl;

	std::cout << "sending AS-IPmapper.py off" << std::endl;
	system(("python3 AS-IPmapper.py " + foldertime + "/top500IPs.txt " + foldertime + "/AStoIP.txt").c_str());
	std::cout << "AS-IPmapper.py joined back" << std::endl;

	std::cout << "sending subset.sh off" << std::endl;
	system(("./subset.sh " + foldertime + "/top500sites.txt " + foldertime + "/nslookups.txt").c_str());	
	std::cout << "subset.sh joined back" << std::endl;

	std::cout << "sending ipv6finder.py off" << std::endl;
	system(("python3 ipv6finder.py " + foldertime + "/nslookups.txt " + foldertime + "/ipv6capablesites.txt").c_str());
	std::cout << "ipv6finder.py joined back" << std::endl;


	/*

	pid_t scraperPID;
	scraperPID = fork();
	if(scraperPID>= 0){
		if(scraperPID == 0){
			char *args[] = {"python3", "topsitescraper.py", "top500sites.txt", NULL};
			std::cout << "I am child process " << scraperPID << " running topsitescraper.py" << std::endl;
			execvp(args[0],args);
		
		}

	}

	*/



	std::cout << "finished" << std::endl;
	return 0;
}
