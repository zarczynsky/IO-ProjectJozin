#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <new>


using namespace std;

class Dane
{
public:
	int i = 0;		//zmienne pomocnicze
	int j = 0;
	int igraf = 0;

	int rozmiar_pliku = 0;
	string znak = "->";
	const string quote = "\"";
	string linia;
	string linia2;
	fstream dane;
	int rozmiar_dynamicznej = 0;


	string graph = "digraph G {";
	string dotPath = "C:\\Users\\Tycjan\\Documents\\release\\bin\\dot.exe"; //link do biblioteki
	string notatnik = "graf_jozin.txt";
	string tempFile = "temp.dot";
	string outFile = "out.png";
};

class Funkcje : public Dane
{
public:
	void draw() {

		graph += "}";
		cout << graph << endl;
		ofstream out;
		out.open(tempFile.c_str(), std::ios::out);
		out << graph << std::endl;
		out.close();

		system((dotPath + " " + tempFile + " -Tpng -o " + outFile).c_str());	//tworzenie grafu
	}
	void polaczenia(string nazwa, string color) {


		rozmiar_dynamicznej = 0;	//zerujemy rozmiar dla wielukrotnego wywolania funkcji

		dane.open(notatnik, ios::in);  //txt od Grzesia

		if (dane.good() == false)
		{
			cout << "Nie mozna otworzyc pliku";
			exit(0);
		}
		else
		{
			ifstream file("graf_jozin.txt");		//sprawdzanie rozmiaru pliku do stworzenia tablic dynamicznych
			while (getline(file, linia2))
				rozmiar_pliku++;

			string* grafs = new string[rozmiar_pliku];	// stringi potrzebne do rysowania grafu w petli
			string* poloczenia = new string[rozmiar_pliku];//tablica do poloczen
			string* wagi = new string[rozmiar_pliku]();//tablica do wag
			for (int i = 0; i < rozmiar_pliku; i++)
				wagi[i] = "0";			//zerujemy tablice wag


			int l_polaczen = 0;
			i = 0;

			while (getline(dane, linia))
			{
				if (linia == nazwa) {
					break;
				}
			}

			i = 0;
			while (getline(dane, linia))          //petla zczytujaca poloczenia miedzy plikami
			{
				poloczenia[i] = linia;
				l_polaczen++;
				i++;
				if (linia == "dane") break;
			}

			i = 0;
			while (getline(dane, linia))         //petla zczytujaca wagi
			{
				wagi[i] = linia;
				rozmiar_dynamicznej++;			//licznik wag jest jednoznaczny z iloscia polaczen
				if (linia == "dane")
				{
					wagi[i] = "0";		//waga od i zeby nie byla rowna "dane"
					break;
				}
				i++;
			}

			string* all = new string[rozmiar_dynamicznej];

			i = 0;
			for (j = 0; j < rozmiar_dynamicznej - 1; j++)	//all to sa te dlugie stringi, które wsadzamy do grafu
			{											//tworzymy ich tyle ile jest polaczen


				if (wagi[j] == "0")								//sprawdzamy czy musimy tworzyc polaczenie czy wolny wezel
				{
					all[j] = quote + poloczenia[i] + quote +  ";\n" +quote + poloczenia[i + 1] + quote;
					grafs[j] = all[j] + ";\n";
					i = i + 2;
				}
				else {

					all[j] = quote + poloczenia[i] + quote +  znak + quote + poloczenia[i + 1] + quote;
					grafs[j] = all[j] + "[label = " + wagi[j] + "];\n";
					i = i + 2;
				}
			}



			for (igraf = 0; igraf < l_polaczen - 1; igraf++)	// tworzenie polecenia do stworzenia grafu w petli
			{
				//tworzenie samych wezlow o kolorze
				graph += "" + quote + poloczenia[igraf] + quote + " [style =filled, color="+color+" ]; \n";
			}
			for (igraf = 0; igraf < rozmiar_dynamicznej; igraf++)
			{
				//dodajemy do polecenia
				graph += grafs[igraf];
			}


			cout << graph;
			delete[] poloczenia;
			delete[] wagi;
			delete[] grafs;
		}

		dane.close();
	}
	void Functions()
	{
		polaczenia("FUNCTIONS", "lightskyblue1");
		draw();
	}
	void Files()
	{
		polaczenia("FILES", "gold1");
		draw();
	}
	void Modules()
	{
		polaczenia("MODULES","burlywood2");
		draw();
	}
	void PlikiFunkcje()
	{
		polaczenia("FILES", "gold1");
		polaczenia("FUNCTIONS", "lightskyblue1");
		draw();

	}
	void PlikiModuly()
	{
		polaczenia("FILES", "gold1");
		polaczenia("MODULES", "burlywood2");
		draw();
	}
	void FunkcjeModuly()
	{
		polaczenia("FUNCTIONS", "lightskyblue1");
		polaczenia("MODULES", "burlywood2");
		draw();
	}
	void FunkcjeModulyPliki()
	{
		polaczenia("FUNCTIONS", "lightskyblue1");
		polaczenia("MODULES", "burlywood2");
		polaczenia("FILES", "gold1");
		draw();
	}
};