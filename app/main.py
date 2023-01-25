from msilib import add_data
import folium
from folium.plugins import MousePosition
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Kuisioner_Individu, User
from . import db

main = Blueprint('homepage', __name__)

@main.route("/")
def home():
    if current_user.is_authenticated:
        return render_template("homepage.html", name=current_user.nama)
    return render_template("homepage.html")

# @main.route("/gis", methods=['GET', 'POST'])
# def gis():
#     map = folium.Map(
#             location=[-1.1265694, 118.6380067], zoom_start=5, tiles="cartodbpositron", min_zoom=5, zoom_control=True
#     )

#     formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
#     MousePosition(
#         position="bottomleft",
#         separator=" | ",
#         empty_string="NaN",
#         lng_first=True,
#         num_digits=20,
#         prefix="Kordinat:",
#         lat_formatter=formatter,
#         lng_formatter=formatter,
#     ).add_to(map)

#     map.save("app/templates/gis-maps.html")
#     return render_template("maps.html")

@main.route("/dashboard")
@login_required
def index():
    return render_template('index.html')

@main.route("/icons")
@login_required
def icons():
    return render_template('icons.html')

@main.route("/forms", methods=['GET', 'POST'])
@main.route("/forms/<id>", methods=['GET','POST'])
@login_required
def forms(id=None):
    if id:
        update = Kuisioner_Individu.query.filter_by(id=id).first()
            
        return render_template('forms.html', row = update, id=id)
    else:
        if request.method == 'POST' :
            edit = request.form.get('edit')
            print (edit)
            if edit:
                update = Kuisioner_Individu.query.get(request.form.get('edit'))

                update.Nomor_KK=request.form['NoKK']
                update.Jumlah_Anggota_Keluarga=request.form['JumlahAK']
                update.Nama_Kepala_Keluarga=request.form['NamaKK']
                update.Jenis_Kelamin_Keluarga=request.form['JKKK']
                update.NIK=request.form['NIK']
                update.Nama_Lengkap=request.form['Namalkp']
                update.Jenis_Kelamin=request.form['JK']
                update.Tempat_Lahir=request.form['tempatlhr']
                update.Tanggal_Lahir=request.form['tgllhr']
                update.Status_Perkawinan=request.form['Skwn']
                update.Agama=request.form['Agama']
                update.Suku=request.form['Suku']
                update.Warga_Negara=request.form['warganeg']
                update.Nomor_Telp=request.form['notelp']
                update.Nomor_Wa=request.form['nowa']
                update.Email=request.form['email']
                update.Media_Sosial=request.form['akunmedsos']
                
                # elif request.form ['submit'] =='deskjob': 
                update.Kondisi_Pekerjaan=request.form['konjob']
                update.Pekerjaan_Utama=request.form['jobut']
                update.Jaminan_Sosial_Ketenagakerjaan=request.form['bpjs']
                update.Penghasilan_Sebulan_Terakhir=request.form['peng1bln']
                update.Pengeluaran_Sebulan_Terakhir=request.form['penlu1bln']
                update.Kepemilikan_Rumah=request.form['keprmh']
                update.Kepemilikan_Lahan_Luas=request.form['keplhn']

                # elif request.form ['submit'] =='deskkes':
                update.Penyakit_Setahun_Terakhir=request.form['penyakit']
                update.Fasilitas_Kesehatan_Dikunjungi=request.form['faskes']
                update.Jumlah_Berapa_Kali_Fasilitas_Kesehatan_Dikunjungi=request.form['jmlhfaskes']
                update.Jaminan_Kesehatan_Asuransi_KIS=request.form['kis']
                update.Disabilitas=request.form['disabil']

                # elif request.form ['submit'] =='deskpend':
                update.Pendidikan_Terakhir=request.form['pendidk']
                update.Bahasa_Digunakan_Dirumah=request.form['bhs']
                update.Bahasa_Digunakan_Disekolah_Kantor_Tempat_Kerja=request.form['bhsskl']
                update.Kerja_Bakti_Setahun_Terakhir=request.form['krjbkti']
                update.Siskamling_Setahun_Terakhir=request.form['siskaeee']
                update.Pesta_Rakyat_atau_Adat_Terakhir_Dilaksanakan=request.form['pestaryt']
                update.Menolong_warga_Mengalami_Kematian_Setahun_Terakhir=request.form['tlngdet']
                update.Menolong_warga_Mengalami_Sakit_Setahun_Terakhir=request.form['tlngskt']
                update.Menolong_warga_Mengalami_Kecelakaan_Setahun_Terakhir=request.form['tlnglaka']

                db.session.commit()
                flash("Data berhasil diubah")

                return redirect(url_for('homepage.tables'))
                
            # if request.form ['submit'] =='deskindiv':
            Nomor_KK=request.form['NoKK']
            Jumlah_Anggota_Keluarga=request.form['JumlahAK']
            Nama_Kepala_Keluarga=request.form['NamaKK']
            Jenis_Kelamin_Keluarga=request.form['JKKK']
            NIK=request.form['NIK']
            Nama_Lengkap=request.form['Namalkp']
            Jenis_Kelamin=request.form['JK']
            Tempat_Lahir=request.form['tempatlhr']
            Tanggal_Lahir=request.form['tgllhr']
            Status_Perkawinan=request.form['Skwn']
            Agama=request.form['Agama']
            Suku=request.form['Suku']
            Warga_Negara=request.form['warganeg']
            Nomor_Telp=request.form['notelp']
            Nomor_Wa=request.form['nowa']
            Email=request.form['email']
            Media_Sosial=request.form['akunmedsos']
            
            # elif request.form ['submit'] =='deskjob': 
            Kondisi_Pekerjaan=request.form['konjob']
            Pekerjaan_Utama=request.form['jobut']
            Jaminan_Sosial_Ketenagakerjaan=request.form['bpjs']
            Penghasilan_Sebulan_Terakhir=request.form['peng1bln']
            Pengeluaran_Sebulan_Terakhir=request.form['penlu1bln']
            Kepemilikan_Rumah=request.form['keprmh']
            Kepemilikan_Lahan_Luas=request.form['keplhn']

            # elif request.form ['submit'] =='deskkes':
            Penyakit_Setahun_Terakhir=request.form['penyakit']
            Fasilitas_Kesehatan_Dikunjungi=request.form['faskes']
            Jumlah_Berapa_Kali_Fasilitas_Kesehatan_Dikunjungi=request.form['jmlhfaskes']
            Jaminan_Kesehatan_Asuransi_KIS=request.form['kis']
            Disabilitas=request.form['disabil']

            # elif request.form ['submit'] =='deskpend':
            Pendidikan_Terakhir=request.form['pendidk']
            Bahasa_Digunakan_Dirumah=request.form['bhs']
            Bahasa_Digunakan_Disekolah_Kantor_Tempat_Kerja=request.form['bhsskl']
            Kerja_Bakti_Setahun_Terakhir=request.form['krjbkti']
            Siskamling_Setahun_Terakhir=request.form['siskaeee']
            Pesta_Rakyat_atau_Adat_Terakhir_Dilaksanakan=request.form['pestaryt']
            Menolong_warga_Mengalami_Kematian_Setahun_Terakhir=request.form['tlngdet']
            Menolong_warga_Mengalami_Sakit_Setahun_Terakhir=request.form['tlngskt']
            Menolong_warga_Mengalami_Kecelakaan_Setahun_Terakhir=request.form['tlnglaka']

            # Analisis Pengeluaran Perkapita
            ldata = int(Pengeluaran_Sebulan_Terakhir) / int(Jumlah_Anggota_Keluarga) 


            add_data_Kuisioner_Individu = Kuisioner_Individu(Analisis_Pengeluaran_Perkapita=ldata,
                                            Nomor_KK=Nomor_KK,
                                            Jumlah_Anggota_Keluarga=Jumlah_Anggota_Keluarga,
                                            Nama_Kepala_Keluarga=Nama_Kepala_Keluarga,
                                            Jenis_Kelamin_Keluarga=Jenis_Kelamin_Keluarga,
                                            NIK=NIK,
                                            Nama_Lengkap=Nama_Lengkap,
                                            Jenis_Kelamin=Jenis_Kelamin,
                                            Tempat_Lahir=Tempat_Lahir,
                                            Tanggal_Lahir=Tanggal_Lahir,
                                            Status_Perkawinan=Status_Perkawinan,
                                            Agama=Agama,
                                            Suku=Suku,
                                            Warga_Negara=Warga_Negara,
                                            Nomor_Telp=Nomor_Telp,
                                            Nomor_Wa=Nomor_Wa,
                                            Email=Email,
                                            Media_Sosial=Media_Sosial,
                                            # Deskjob
                                            Kondisi_Pekerjaan=Kondisi_Pekerjaan,
                                            Pekerjaan_Utama=Pekerjaan_Utama,
                                            Jaminan_Sosial_Ketenagakerjaan=Jaminan_Sosial_Ketenagakerjaan,
                                            Penghasilan_Sebulan_Terakhir=Penghasilan_Sebulan_Terakhir,
                                            Pengeluaran_Sebulan_Terakhir=Pengeluaran_Sebulan_Terakhir,
                                            Kepemilikan_Rumah=Kepemilikan_Rumah,
                                            Kepemilikan_Lahan_Luas=Kepemilikan_Lahan_Luas,
                                            # Deskkes
                                            Penyakit_Setahun_Terakhir=Penyakit_Setahun_Terakhir,
                                            Fasilitas_Kesehatan_Dikunjungi=Fasilitas_Kesehatan_Dikunjungi,
                                            Jumlah_Berapa_Kali_Fasilitas_Kesehatan_Dikunjungi=Jumlah_Berapa_Kali_Fasilitas_Kesehatan_Dikunjungi,
                                            Jaminan_Kesehatan_Asuransi_KIS=Jaminan_Kesehatan_Asuransi_KIS,
                                            Disabilitas=Disabilitas,
                                            # Deskpend
                                            Pendidikan_Terakhir=Pendidikan_Terakhir,
                                            Bahasa_Digunakan_Dirumah=Bahasa_Digunakan_Dirumah,
                                            Bahasa_Digunakan_Disekolah_Kantor_Tempat_Kerja=Bahasa_Digunakan_Disekolah_Kantor_Tempat_Kerja,
                                            Kerja_Bakti_Setahun_Terakhir=Kerja_Bakti_Setahun_Terakhir,
                                            Siskamling_Setahun_Terakhir=Siskamling_Setahun_Terakhir,
                                            Pesta_Rakyat_atau_Adat_Terakhir_Dilaksanakan=Pesta_Rakyat_atau_Adat_Terakhir_Dilaksanakan,
                                            Menolong_warga_Mengalami_Kematian_Setahun_Terakhir=Menolong_warga_Mengalami_Kematian_Setahun_Terakhir,
                                            Menolong_warga_Mengalami_Sakit_Setahun_Terakhir=Menolong_warga_Mengalami_Sakit_Setahun_Terakhir,
                                            Menolong_warga_Mengalami_Kecelakaan_Setahun_Terakhir=Menolong_warga_Mengalami_Kecelakaan_Setahun_Terakhir,

                                            )
                # db.session.add(add_data_deskindiv)
                                        

                
                
                # add_data_deskjob = Kuisioner_Individu( ,

                #                                 )
                # db.session.add(add_data_deskjob)

            # elif request.form ['submit'] =='deskkes':
                
                # add_data_deskkes = Kuisioner_Individu( ,
                #                                 )
                # db.session.add(add_data_deskkes)

            # elif request.form ['submit'] =='deskpend':

                #  add_data_Kuisioner_Individu = Kuisioner_Individu( )
                                                
            db.session.add(add_data_Kuisioner_Individu)

            db.session.commit()
            flash("Data Telah Dimasukkan :)")        

        return render_template('forms.html')

@main.route("/tables", methods=['GET','POST'])
@login_required
def tables():
    Kuisindiv = Kuisioner_Individu.query.all()

    if request.method == 'POST' :
        edit = request.form.get('ubah')
        if edit:
            id = request.form.get('ubah')
            return redirect(url_for('homepage.forms', id=id))
        
    return render_template('tables.html', Kuisioner_Individu=Kuisindiv)


@main.route("/hasil_analisis")
@login_required
def hasil_analisis():
    Kuisindiv = Kuisioner_Individu.query.all()
    return render_template('hasil_analisis.html',Kuisioner_Individu=Kuisindiv)





@main.route("/calendar")
@login_required
def calendar():
    return render_template('calendar.html')

@main.route("/profile")
@login_required
def profile():
    return render_template('profile.html')


@main.route("/login")
@login_required
def login():
    return render_template('login.html')

@main.route("/register")
@login_required
def register():
    return render_template('register.html')

@main.route("/usermanager")
@login_required
def usermanager():
    user = User.query.all()
    return render_template('usermanager.html',user=user)

@ main.route("/gis", methods=['GET', 'POST'])
@ main.route("/gis/<id>", methods=['GET', 'POST'])
def gis(id=None):
    if id:
        data = Peta_Desa.query.filter_by(id=id).first()

        layer = gpd.read_file(data.json)
        layer = layer.to_crs("EPSG:4326")

        m = folium.Map(location=[-1.1265694, 118.6380067],
                   zoom_start=5, min_zoom=5)

        for x in layer.index:
            color = np.random.randint(16, 256, size=3)
            color = [str(hex(i))[2:] for i in color]
            color = '#'+''.join(color).upper()
            layer.at[x, 'color'] = color

        def style(feature):
            return {
                'fillColor': feature['properties']['color'],
                'color': feature['properties']['color'],
                'weight': 1,
                'fillOpacity': 0.7
            }

        gjson = folium.GeoJson(layer, name=data.desa, style_function=style).add_to(m)

        m.fit_bounds(gjson.get_bounds())

        folium.Popup(data.desa).add_to(gjson)

        formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
        MousePosition(
            position="bottomleft",
            separator=" | ",
            empty_string="NaN",
            lng_first=True,
            num_digits=20,
            prefix="Kordinat:",
            lat_formatter=formatter,
            lng_formatter=formatter,
        ).add_to(m)

        tile_layer = folium.TileLayer(
            tiles="http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}",
            attr='google.com',
            max_zoom=19,
            name='darkmatter',
            control=False,
            opacity=1
        )
        tile_layer.add_to(m)

        m.save("app/templates/gis-maps.html")
        return render_template("maps.html", data=data, id=id)

    m = folium.Map(location=[-1.1265694, 118.6380067],
                   zoom_start=5, min_zoom=5)

    formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
    MousePosition(
        position="bottomleft",
        separator=" | ",
        empty_string="NaN",
        lng_first=True,
        num_digits=20,
        prefix="Kordinat:",
        lat_formatter=formatter,
        lng_formatter=formatter,
    ).add_to(m)

    tile_layer = folium.TileLayer(
        tiles="http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}",
        attr='google.com',
        max_zoom=19,
        name='darkmatter',
        control=False,
        opacity=1
    )
    tile_layer.add_to(m)

    m.save("app/templates/gis-maps.html")
    return render_template("maps.html")

@ main.route("/inputdata")
@ login_required
def inputdata():
    # image = None
    # if current_user.img:
    #     image = base64.b64encode(current_user.img).decode('ascii')
    active = 'active'
    return render_template("input-data.html", name=current_user.nama, level=current_user.lvl, input_data_navbar=active)

@ main.route("/inputdatauser")
@ login_required
def inputdatauser():
    # image = None
    # if current_user.img:
    #     image = base64.b64encode(current_user.img).decode('ascii')
    active = 'active'
    return render_template("input-data-user.html", name=current_user.nama, level=current_user.lvl, input_data_navbar=active)

@ main.route("/input-data/data-desa")
@ login_required
def input_data_desa():
    active = 'active'

    image = None
    if current_user.img:
        image = base64.b64encode(current_user.img).decode('ascii')

    provinsi = Provinsi.query.all()
    all_data = Desa.query.all()
    return render_template("input-data-desa.html", img=image, name=current_user.nama, level=current_user.lvl, input_data_desa_navbar=active, input_data_master_navbar=active, provinsi=provinsi, desa=all_data)


@ main.route("/input-data/data-desa/live-search", methods=['GET', 'POST'])
@ login_required
def live_search_data_desa():
    if request.method == 'POST':
        id = request.form['kecamatan_response']
        desa = Desa.query.filter(Desa.id_kec.like(id))
    return jsonify({'htmlresponse': render_template('data-desa-response.html', desa=desa)})


@ main.route("/input-data/data-desa/add", methods=['POST'])
@ login_required
def input_data_desa_add():
    if request.method == 'POST':
        id_kec = request.form['kecamatan']
        id_desa = request.form['id']
        id = id_kec+id_desa
        nama = request.form['nama']

        desa = Desa.query.filter_by(id=id).first()
        if desa:
            flash('ID telah digunakan')
            return redirect(url_for('main.input_data_desa'))

        add_Data = Desa(id=id, id_kec=id_kec, nama=nama)

        db.session.add(add_Data)
        db.session.commit()
        flash("Data berhasil ditambahkan")

        return redirect(url_for('main.input_data_desa'))


@ main.route("/input-data/data-desa/update", methods=['GET', 'POST'])
@ login_required
def input_data_desa_update():
    if request.method == 'POST':
        update = Desa.query.get(request.form.get('id_desa'))
        update.nama = request.form['nama']

        db.session.commit()
        flash("Data berhasil diubah")

        return redirect(url_for('main.input_data_desa'))


@ main.route("/input-data/data-desa/delete", methods=['GET', 'POST'])
@ login_required
def input_data_desa_delete():
    id = request.form['id']
    delete = Desa.query.get(id)

    db.session.delete(delete)
    db.session.commit()
    flash("Data berhasil dihapus")

    return redirect(url_for('main.input_data_desa'))


@ main.route("/input-data/data-kecamatan")
@ login_required
def input_data_kecamatan():
    active = 'active'

    image = None
    if current_user.img:
        image = base64.b64encode(current_user.img).decode('ascii')

    provinsi = Provinsi.query.all()
    all_data = Kecamatan.query.all()
    return render_template("input-data-kecamatan.html", img=image, name=current_user.nama, level=current_user.lvl, input_data_kecamatan_navbar=active, input_data_master_navbar=active, provinsi=provinsi, kecamatan=all_data)


@ main.route("/input-data/data-kecamatan/live-search", methods=['GET', 'POST'])
@ login_required
def live_search_data_kecamatan():
    if request.method == 'POST':
        id = request.form['kabupaten_response']
        kecamatan = Kecamatan.query.filter(Kecamatan.id_kab.like(id))
    return jsonify({'htmlresponse': render_template('data-kecamatan-response.html', kecamatan=kecamatan)})


@ main.route("/input-data/data-kecamatan/add", methods=['POST'])
@ login_required
def input_data_kecamatan_add():
    if request.method == 'POST':
        id_kab = request.form['kabupaten']
        id_kec = request.form['id']
        id = id_kab+id_kec
        nama = request.form['nama']

        kec = Kecamatan.query.filter_by(id=id).first()
        if kec:
            flash('ID telah digunakan')
            return redirect(url_for('main.input_data_kecamatan'))

        add_Data = Kecamatan(id=id, id_kab=id_kab, nama=nama)

        db.session.add(add_Data)
        db.session.commit()
        flash("Data berhasil ditambahkan")

        return redirect(url_for('main.input_data_kecamatan'))


@ main.route("/input-data/data-kecamatan/update", methods=['GET', 'POST'])
@ login_required
def input_data_kecamatan_update():
    if request.method == 'POST':
        update = Kecamatan.query.get(request.form.get('id_kecamatan'))
        update.nama = request.form['nama']

        db.session.commit()
        flash("Data berhasil diubah")

        return redirect(url_for('main.input_data_kecamatan'))


@ main.route("/input-data/data-kecamatan/delete", methods=['GET', 'POST'])
@ login_required
def input_data_kecamatan_delete():
    id = request.form['id']
    delete = Kecamatan.query.get(id)

    db.session.delete(delete)
    db.session.commit()
    flash("Data berhasil dihapus")

    return redirect(url_for('main.input_data_kecamatan'))


@ main.route("/input-data/data-kabupaten")
@ login_required
def input_data_kabupaten():
    active = 'active'

    image = None
    if current_user.img:
        image = base64.b64encode(current_user.img).decode('ascii')

    provinsi = Provinsi.query.all()
    all_data = Kabupaten.query.all()
    return render_template("input-data-kabupaten.html", img=image, name=current_user.nama, level=current_user.lvl, input_data_kabupaten_navbar=active, input_data_master_navbar=active, provinsi=provinsi, kabupaten=all_data)


@ main.route("/input-data/data-kabupaten/live-search", methods=['GET', 'POST'])
@ login_required
def live_search_data_kabupaten():
    if request.method == 'POST':
        id = request.form['provinsi_response']
        kabupaten = Kabupaten.query.filter(Kabupaten.id_prov.like(id))
    return jsonify({'htmlresponse': render_template('data-kabupaten-response.html', kabupaten=kabupaten)})


@ main.route("/input-data/data-kabupaten/add", methods=['POST'])
@ login_required
def input_data_kabupaten_add():
    if request.method == 'POST':
        id_prov = request.form['provinsi']
        id_kab = request.form['id']
        id = id_prov+id_kab
        nama = request.form['nama']

        kab = Kabupaten.query.filter_by(id=id).first()
        if kab:
            flash('ID telah digunakan')
            return redirect(url_for('main.input_data_kabupaten'))

        add_Data = Kabupaten(id=id, id_prov=id_prov, nama=nama)

        db.session.add(add_Data)
        db.session.commit()
        flash("Data berhasil ditambahkan")

        return redirect(url_for('main.input_data_kabupaten'))


@ main.route("/input-data/data-kabupaten/update", methods=['GET', 'POST'])
@ login_required
def input_data_kabupaten_update():
    if request.method == 'POST':
        update = Kabupaten.query.get(request.form.get('id_kabupaten'))
        update.nama = request.form['nama']

        db.session.commit()
        flash("Data berhasil diubah")

        return redirect(url_for('main.input_data_kabupaten'))


@ main.route("/input-data/data-kabupaten/delete", methods=['GET', 'POST'])
@ login_required
def input_data_kabupaten_delete():
    id = request.form['id']
    delete = Kabupaten.query.get(id)

    db.session.delete(delete)
    db.session.commit()
    flash("Data berhasil dihapus")

    return redirect(url_for('main.input_data_kabupaten'))


@ main.route("/input-data/data-provinsi")
@ login_required
def input_data_provinsi():
    active = 'active'

    image = None
    if current_user.img:
        image = base64.b64encode(current_user.img).decode('ascii')

    all_data = Provinsi.query.all()
    return render_template("input-data-provinsi.html", img=image, name=current_user.nama, level=current_user.lvl, input_data_provinsi_navbar=active, input_data_master_navbar=active, provinsi=all_data)

@ main.route("/input-data/data-provinsi/add", methods=['POST'])
@ login_required
def input_data_provinsi_add():
    if request.method == 'POST':
        id = request.form['id']
        nama = request.form['nama']

        prov = Provinsi.query.filter_by(id=id).first()
        if prov:
            flash('ID telah digunakan')
            return redirect(url_for('main.input_data_provinsi'))

        add_Data = Provinsi(id=id, nama=nama)

        db.session.add(add_Data)
        db.session.commit()
        flash("Data berhasil ditambahkan")

        return redirect(url_for('main.input_data_provinsi'))


@ main.route("/input-data/data-provinsi/update", methods=['GET', 'POST'])
@ login_required
def input_data_provinsi_update():
    if request.method == 'POST':
        update = Provinsi.query.get(request.form.get('id_provinsi'))
        update.nama = request.form['nama']

        db.session.commit()
        flash("Data berhasil diubah")

        return redirect(url_for('main.input_data_provinsi'))


@ main.route("/input-data/data-provinsi/delete", methods=['GET', 'POST'])
@ login_required
def input_data_provinsi_delete():
    id = request.form['id']
    delete = Provinsi.query.get(id)

    db.session.delete(delete)
    db.session.commit()
    flash("Data berhasil dihapus")

    return redirect(url_for('main.input_data_provinsi'))


@ main.route("/input-data/peta-desa")
@ login_required
def input_data_peta_desa():
    active = 'active'

    image = None
    if current_user.img:
        image = base64.b64encode(current_user.img).decode('ascii')

    provinsi = Provinsi.query.all()
    all_data = Peta_Desa.query.all()
    return render_template("input-data-peta-desa.html", img=image, name=current_user.nama, level=current_user.lvl, input_data_peta_desa_navbar=active, input_data_spasial_navbar=active, provinsi=provinsi, peta_desa=all_data)


@ main.route("/input-data/peta-desa/add", methods=['GET', 'POST'])
@ login_required
def input_data_peta_desa_add():
    if request.method == 'POST':
        prov = request.form['provinsi']
        kab = request.form['kabupaten']
        kec = request.form['kecamatan']
        des = request.form['desa']
        file = request.files['json']

        provinsi = Provinsi.query.filter_by(id=prov).first()
        kabupaten = Kabupaten.query.filter_by(id=kab).first()
        kecamatan = Kecamatan.query.filter_by(id=kec).first()
        desa = Desa.query.filter_by(id=des).first()
        peta_desa = Peta_Desa.query.filter_by(id=des).first()
        
        if peta_desa:
            flash('ID telah digunakan')
            return redirect(url_for('main.input_data_pupuk'))

        json = "{}.json".format(des)
        nama = "{}, {}, Kec. {}, Desa {}".format(provinsi.nama, kabupaten.nama, kecamatan.nama, desa.nama)
        extfile = file.filename.rsplit('.', 1)[1].lower()

        file.save(os.path.join("app/static/json/temporary", "{}.{}".format(des, extfile)))
        patoolib.extract_archive("app/static/json/temporary/{}.{}".format(des, extfile), outdir="app/static/json/temporary/")

        dir = 'app/static/json/temporary'
        search_shp = [f for f in os.listdir(dir) if f.endswith(".shp")]

        gjson = gpd.read_file("app/static/json/temporary/{}".format(search_shp[0]))
        gjson.to_file("app/static/json/temporary/{}".format(json), driver='GeoJSON')
        gjson = gjson.to_json()
        add_Data = Peta_Desa(id=des, nama=nama, json=gjson)

        db.session.add(add_Data)
        db.session.commit()

        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))

        flash("Data berhasil ditambahkan")

        return redirect(url_for('main.input_data_peta_desa'))


@ main.route("/input-data/peta-desa/update", methods=['GET', 'POST'])
@ login_required
def input_data_peta_desa_update():
    if request.method == 'POST':
        update = Peta_Desa.query.get(request.form.get('id_desa'))
        update.nama = request.form['nama']
        id = request.form['id_desa']
        file = request.files['json']

        if file:
            json = "{}.json".format(id)
            extfile = file.filename.rsplit('.', 1)[1].lower()

            file.save(os.path.join("app/static/json/temporary", "{}.{}".format(id, extfile)))
            patoolib.extract_archive("app/static/json/temporary/{}.{}".format(id, extfile), outdir="app/static/json/temporary/")

            dir = 'app/static/json/temporary'
            search_shp = [f for f in os.listdir(dir) if f.endswith(".shp")]

            gjson = gpd.read_file("app/static/json/temporary/{}".format(search_shp[0]))
            gjson.to_file("app/static/json/temporary/{}".format(json), driver='GeoJSON')
            gjson = gjson.to_json()

            update.json = gjson

            for f in os.listdir(dir):
                os.remove(os.path.join(dir, f))

        db.session.commit()
        flash("Data berhasil diubah")

        return redirect(url_for('main.input_data_peta_desa'))


@ main.route("/input-data/peta-desa/delete", methods=['GET', 'POST'])
@ login_required
def input_data_peta_desa_delete():
    id = request.form['id']
    delete = Peta_Desa.query.get(id)

    db.session.delete(delete)
    db.session.commit()
    flash("Data berhasil dihapus")

    return redirect(url_for('main.input_data_peta_desa'))

@ main.route("/input-data/data-jumlah-penduduk")
@ login_required
def input_data_jumlah_penduduk():
    active = 'active'

    image = None
    if current_user.img:
        image = base64.b64encode(current_user.img).decode('ascii')

    provinsi = Provinsi.query.all()
    all_data = Jumlah_Penduduk.query.all()
    return render_template("input-data-gapoktan.html", img=image, name=current_user.nama, level=current_user.lvl, input_data_jumlah_penduduk_navbar=active, input_data_desa_navbar=active, jumlah_penduduk=all_data, provinsi=provinsi)


@ main.route("/input-data/data-jumlah-penduduk/add", methods=['POST'])
@ login_required
def input_data_jumlah_penduduk_add():
    if request.method == 'POST':
        id = request.form['desa']
        nama = request.form['nama']
        jumlah = request.form['jumlah']

        gapoktan = Gapoktan.query.filter_by(id=id).first()
        if gapoktan:
            flash('ID telah digunakan')
            return redirect(url_for('main.input_data_gapoktan'))

        add_Data = Gapoktan(id=id, id_desa=id_desa, nama=nama, ketua=ketua, telp=telp, no_sk=no_sk)

        db.session.add(add_Data)
        db.session.commit()
        flash("Data berhasil ditambahkan")

        return redirect(url_for('main.input_data_gapoktan'))





