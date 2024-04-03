int main(){
    int nOndas, inicio, clones, zetsus, totalN=0;
    bool perdeu = false;

    cin >> nOndas >> inicio;
    cin >> zetsus >> clones;

    clones += inicio;
    while (nOndas != 0){
        cin >> zetsus >> clones;
        totalN += clones;
        if (zetsus > totalN){
            perdeu = true;
        }
        totalN -= zetsus;
        nOndas--;
    }

    if (!perdeu){
        cout << "Naruto defendeu a vila";
    } else {
        cout << "Madara venceu";
    }
    return 0;
}