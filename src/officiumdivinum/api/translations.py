"""
Translations of invariant bits.

In the long run these should be serialised into the database and read
out at object creation.
"""
from ..objects.datastructures import Blessing
from ..objects.datastructures import Collect
from ..objects.datastructures import Hymn
from ..objects.datastructures import Reading
from ..objects.datastructures import Responsory

invariants = {
    "latin": {
        "regi saeculorum": Reading(
            "regi saeculorum",
            "1Tim1:17",
            [
                "Regi sæculórum immortáli et invisíbili, soli Deo honor et glória in sǽcula sæculórum. Amen. "
            ],
        ),
        "christe, fili dei per annum": Responsory(
            [
                ("R.br.", "Christe, Fili Dei vivi, * miserére nobis."),
                ("R.", "Christe, Fili Dei vivi, * miserére nobis."),
                ("V.", "Qui sedes ad déxteram Pátris."),
                ("R.", "Miserére nobis."),
                ("", "Gloria Patri et Filio * et Spiritui Sancto"),
                (
                    "",
                    "Sicut erat in principio, et nunc et semper *"
                    "et in saecula saeculorum.  Amen.",
                ),
                ("R." "Christe, Fili Dei vivi, * miserére nobis."),
            ]
        ),
        "exurge christe per annum": Responsory(
            [
                ("V.", "Exsúrge, Christe, ádjuva nos."),
                ("R.", "Et líbera nos propter nomen tuum."),
            ]
        ),
        "domine exaudi": Responsory(
            [
                ("V.", "Domine exaudi orationem meam"),
                ("R.", "et clamor meus ad te veniat"),
            ]
        ),
        "oremus": "Orémus.",
        "per dominum nostrum": "Per Dóminum nostrum Jesum Christum, Fílium tuum: qui tecum vivit et regnat in unitáte Spíritus Sancti, Deus, per ómnia sǽcula sæculórum.",
        "domine deus omnipotens": Collect(
            "Dómine Deus omnípotens, qui ad princípium hujus diéi nos perveníre fecísti: tua nos hódie salva virtúte; ut in hac die ad nullum declinémus peccátum, sed semper ad tuam justítiam faciéndam nostra procédant elóquia, dirigántur cogitatiónes et ópera.",
            "Per Dóminum nostrum Jesum Christum, Fílium tuum: qui tecum vivit et regnat in unitáte Spíritus Sancti, Deus, per ómnia sǽcula sæculórum.",
        ),
        "sancta maria et omnes": Collect(
            "Sancta María et omnes Sancti intercédant pro nobis ad Dóminum, ut nos mereámur ab eo adjuvári et salvári, qui vivit et regnat in sǽcula sæculórum.",
            "",
        ),
        "gloria": Responsory(
            [
                ("V.", "Glória Patri, et Fílio, * et Spirítui Sancto."),
                (
                    "R.",
                    "Sicut erat in princípio, et nunc, et semper, * et in sǽcula sæculórum. Amen.",
                ),
            ]
        ),
        "kyrie": "Kýrie, eléison. Christe, eléison. Kýrie, eléison.",
        "pater": Responsory(
            [
                (
                    "",
                    "Pater noster, qui es in cælis, sanctificétur nomen tuum: advéniat regnum tuum: fiat volúntas tua, sicut in cælo et in terra.  Panem nostrum cotidiánum da nobis hódie: et dimítte nobis débita nostra, sicut et nos dimíttimus debitóribus nostris:",
                ),
                ("V.", "Et ne nos indúcas in tentatiónem:"),
                ("R.", "Sed líbera nos a malo."),
            ]
        ),
        "respice": Responsory(
            [
                (
                    "V.",
                    "Réspice in servos tuos, Dómine, et in ópera tua, et dírige fílios eórum.",
                ),
                (
                    "R.",
                    "Et sit splendor Dómini Dei nostri super nos, et ópera mánuum nostrárum dírige super nos, et opus mánuum nostrárum dírige.",
                ),
            ]
        ),
        "dirigere et sanctificare": Collect(
            "Dirígere et sanctificáre, régere et gubernáre dignáre, Dómine Deus, Rex cæli et terræ, hódie corda et córpora nostra, sensus, sermónes et actus nostros in lege tua, et in opéribus mandatórum tuórum: ut hic et in ætérnum, te auxiliánte, salvi et líberi esse mereámur, Salvátor mundi: Qui vivis et regnas in sǽcula sæculórum.",
            "",
        ),
        "iube domine": Responsory([("V.", "Jube, domne, benedícere.")]),
        "dies et actus": Blessing(
            "Dies et actus nostros in sua pace dispónat Dóminus omnípotens. Amen."
        ),
        "adjutorium": Responsory(
            [
                ("V.", "Adjutórium nóstrum + in nómine Dómini."),
                ("R.", "Qui fecit cælum et terram."),
            ]
        ),
        "dominus nos benedicat": Blessing(
            "Dóminus nos benedícat, + et ab omni malo deféndat, et ad vitam perdúcat ætérnam. Et fidélium ánimæ per misericórdiam Dei requiéscant in pace."
        ),
        "Deus in adjutorium": Responsory(
            [
                ("V.", "Deus + in adjutórium meum inténde."),
                ("R." "Dómine, ad adjuvándum me festína."),
            ]
        ),
        "laus tibi": "Laus tibi, Dómine, Rex ætérnæ glóriæ.",
        "iam lucis": Hymn(
            "Iam Lucis",
            [
                [
                    "Jam lucis orto sídere,",
                    "Deum precémur súpplices,",
                    "Ut in diúrnis áctibus",
                    "Nos servet a nocéntibus.",
                ],
                [
                    "Linguam refrénans témperet,",
                    "Ne litis horror ínsonet:",
                    "Visum fovéndo cóntegat,",
                    "Ne vanitátes háuriat.",
                ],
                [
                    "Sint pura cordis íntima,",
                    "Absístat et vecórdia;",
                    "Carnis terat supérbiam",
                    "Potus cibíque párcitas.",
                ],
                [
                    "Ut, cum dies abscésserit,",
                    "Noctémque sors redúxerit,",
                    "Mundi per abstinéntiam",
                    "Ipsi canámus glóriam.",
                ],
                [
                    "Deo Patri sit glória,",
                    "Ejúsque selfoli Fílio,",
                    "Cum Spíritu Paráclito,",
                    "Nunc et per omne sǽculum.",
                    "Amen.",
                ],
            ],
        ),
    }
}
